from app import app
from models import db, Pet


with app.app_context():
    db.drop_all()
    db.create_all()

    Pet.query.delete()

    p1 = Pet(name="Roxy", species="dog", photo_url="https://www.akc.org/wp-content/uploads/2017/11/German-Shepherd-on-White-00.jpg", age=13, notes="Not Aggressive", available=True)
    p2 = Pet(name="Ellie", species="dog", photo_url="https://dogtime.com/wp-content/uploads/sites/12/2019/08/GettyImages-173255251-e1692542655509.jpg", age=2, notes="Playful", available=False)
    p3 = Pet(name="Porky", species="pig", photo_url="https://i.natgeofe.com/k/23e409f9-4699-46f0-a645-5cc1f5040363/pig-full-body_2x1.jpg", age=3, notes="Eats a LOT", available=True)
    p4 = Pet(name="Larry", species="water buffalo", photo_url="https://site-547756.mozfiles.com/files/547756/medium/Water_Buffalo.jpg", age=26, notes="Very Large", available=True)
    p5 = Pet(name="Janice", species="llama", photo_url="https://t4.ftcdn.net/jpg/05/65/45/89/360_F_565458941_DUcW8dLHH3DYqoggUOXBdaZwfdktCHmI.jpg", age=15, notes="Likes to spit and make weird faces", available=True)
    p6 = Pet(name="Lucy", species="cat", photo_url="https://www.thesprucepets.com/thmb/D7ZYblr0r0dq4RtxpS8U9ZwNrCg=/6277x0/filters:no_upscale():strip_icc()/all-about-tabby-cats-4145476-hero-d6eb349cbacb4c7193007b49ead874ff.jpg", age=4, notes="lazy bones", available=False)

    db.session.add_all([p1,p2,p3,p4,p5,p6])
    db.session.commit()