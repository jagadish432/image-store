from db.db import *


def safe_commit():
    try:
        print("writing to db")
        db.session.commit()
        print("written successfully")
    except Exception as e:
        print(str(e))
        db.session.rollback()
        raise


# store blob data of an image into the database
def write_to_db(filename, content, password_protected, password):
    image = ImageStore(filename, content, password_protected, password)
    db.session.add(image)
    safe_commit()
    return image.shortenedURL


# fetch image from db and return to the requested user
def get_from_db(imageURL):
    image = ImageStore.query.filter_by(shortenedURL=imageURL).one_or_none()
    if image is None:
        return False, "Image doesn't exist, try with a different URL"

    return True, image


# increments visit by 1 for the particular image
def increment_visit(image):
    image.visitsCount += 1
    safe_commit()
