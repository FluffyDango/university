from .ner_processor import get_entities
from .ocr_processor import scan_text
from .filter_image import open_and_filter_image
from concurrent.futures import ThreadPoolExecutor, as_completed

def send_images(image_paths: list) -> list:
    results = []
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(process_image, image) for image in image_paths]
        # Iterate through the completed futures
        for future in as_completed(futures):
            result = future.result()
            results.append(result)
    return results

def process_image(image_path: str) -> dict:
    image = open_and_filter_image(image_path)
    if image is None:
        return {}
    
    scanned_text = scan_text(image)
    if scanned_text == "":
        return {}
        
    result = get_entities(scanned_text)

    return result

