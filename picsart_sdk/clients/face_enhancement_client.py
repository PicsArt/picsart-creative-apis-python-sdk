from picsart_sdk.api_response import ApiResponse
from picsart_sdk.clients.base.image_base_client import ImageBaseClient
from picsart_sdk.clients.requests_models import PicsartImage, FaceEnhancementRequest


class FaceEnhancementClient(ImageBaseClient):

    @property
    def endpoint(self):
        return "enhance/face"

    def face_enhancement(self, request: FaceEnhancementRequest) -> ApiResponse:
        return self.post(request=request)

    def face_enhancement_from_path(
        self,
        file_path: str,
    ) -> ApiResponse:
        return self.face_enhancement(
            request=FaceEnhancementRequest(
                image=PicsartImage(image_path=file_path),
            )
        )

    def face_enhancement_from_url(
        self,
        url: str,
    ) -> ApiResponse:
        return self.face_enhancement(
            request=FaceEnhancementRequest(image=PicsartImage(image_url=url))
        )


class AsyncFaceEnhancementClient(FaceEnhancementClient):

    async def face_enhancement(self, request: FaceEnhancementRequest) -> ApiResponse:
        return await self.async_post(request=request)

    async def face_enhancement_from_path(self, file_path: str) -> ApiResponse:
        return await self.face_enhancement(
            request=FaceEnhancementRequest(
                image=PicsartImage(image_path=file_path),
            )
        )

    async def face_enhancement_from_url(self, url: str) -> ApiResponse:
        return await self.face_enhancement(
            request=FaceEnhancementRequest(
                image=PicsartImage(image_url=url),
            )
        )
