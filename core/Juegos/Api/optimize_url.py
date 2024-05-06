from cloudinary import CloudinaryImage, api


def optimize_url(image_id: str) -> str:
    image_base = CloudinaryImage(image_id)
    image_optimized = image_base.build_url(
        transformation=[
            {"gravity": "auto", "crop": "fill"},
            {"quality": "auto", "fetch_format": "webp"},
        ]
    )
    return image_optimized
