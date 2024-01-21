from rest_framework.test import APITestCase
from . import models
from users.models import User


class TestAmenities(APITestCase):
    NAME = "Amenity Test"
    DESC = "Amenity Des"

    URL = "/api/v1/rooms/amenities/"

    def setUp(self):
        models.Amenity.objects.create(
            name=self.NAME,
            description=self.DESC,
        )

    def test_all_amenities(self):
        response = self.client.get(self.URL)
        data = response.json()

        self.assertEqual(
            response.status_code,
            200,
            "Status code isn't 200.",
        )
        self.assertIsInstance(
            data,
            list,
        )
        self.assertEqual(
            len(data),
            1,
        )
        self.assertEqual(
            data[0]["name"],
            self.NAME,
        )
        self.assertEqual(
            data[0]["description"],
            self.DESC,
        )


def test_create_amenity(self):
    new_amenity_name = "New Amenity"
    new_amenity_description = "New Amenity desc."

    response = self.client.post(
        self.URL,
        data={
            "name": new_amenity_name,
            "description": new_amenity_description,
        },
    )
    data = response.json()

    self.assertEqual(
        response.status_code,
        200,
        "Not 200 status code",
    )
    self.assertEqual(
        data["name"],
        new_amenity_name,
    )
    self.assertEqual(
        data["description"],
        new_amenity_description,
    )

    response = self.client.post(self.URL)
    data = response.json()

    self.assertEqual(response.status_code, 400)
    self.assertIn("name", data)


class TestAmenity(APITestCase):
    # 테스트에 사용할 Amenity의 이름과 설명을 설정합니다.
    NAME = "Test Amenity"
    DESC = "Test Desc"

    def setUp(self):
        # 테스트 실행 전에 테스트용 Amenity 객체를 생성합니다.
        self.amenity = models.Amenity.objects.create(
            name=self.NAME,
            description=self.DESC,
        )

    def test_amenity_not_found(self):
        # 존재하지 않는 Amenity ID로 GET 요청을 보내어 404 오류를 확인합니다.
        response = self.client.get("/api/v1/rooms/amenities/9999")
        self.assertEqual(response.status_code, 404)

    def test_get_amenity(self):
        # 생성된 Amenity에 대해 GET 요청을 보내어 정보를 확인합니다.
        response = self.client.get(f"/api/v1/rooms/amenities/{self.amenity.id}")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        # 응답 데이터에서 Amenity의 이름과 설명이 기대한 값과 일치하는지 확인합니다.
        self.assertEqual(data["name"], self.NAME)
        self.assertEqual(data["description"], self.DESC)

    def test_put_amenity(self):
        # Amenity를 수정하기 위해 PUT 요청을 보냅니다.
        updated_name = "Updated Amenity"
        updated_desc = "Updated Desc"
        response = self.client.put(
            f"/api/v1/rooms/amenities/{self.amenity.id}",
            data={"name": updated_name, "description": updated_desc},
            format="json",
        )

        self.assertEqual(response.status_code, 200)
        data = response.json()
        # 응답 데이터에서 Amenity의 이름과 설명이 업데이트된 값과 일치하는지 확인합니다.
        self.assertEqual(data["name"], updated_name)
        self.assertEqual(data["description"], updated_desc)

    def test_delete_amenity(self):
        # Amenity를 삭제하기 위해 DELETE 요청을 보냅니다.
        response = self.client.delete(f"/api/v1/rooms/amenities/{self.amenity.id}")
        self.assertEqual(response.status_code, 204)

        # 삭제 후 해당 Amenity ID로 GET 요청을 보내어 404 오류를 확인합니다.
        response = self.client.get(f"/api/v1/rooms/amenities/{self.amenity.id}")
        self.assertEqual(response.status_code, 404)


class TestRooms(APITestCase):
    def setUp(self):
        user = User.objects.create(
            username="test",
        )
        user.set_password("123")
        user.save()
        self.user = user

    def test_create_room(self):
        response = self.client.post("/api/v1/rooms/")

        self.assertEqual(response.status_code, 403)

        self.client.force_login(
            self.user,
        )
