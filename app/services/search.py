import os
from config import config


def __check_tags_matching(query: str, filename: str) -> bool:
    filename = filename.lower()
    tags = query.split(' ')
    return all(map(lambda tag: tag.lower() in filename, tags))


def find_images(query: str) -> [str]:
    result = []
    for root, dirs, files in os.walk(config.IMAGES_FOLDER):
        for filename in files:
            if __check_tags_matching(query, filename):
                full_path = os.path.join(root[len(config.IMAGES_FOLDER):], filename)
                result.append({
                    "full_path": full_path,
                    "filename": filename,
                    "url": "/image/?filename=" + full_path
                })
    return result
