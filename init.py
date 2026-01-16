from db import Base, engine

def init_db():
    Base.metadata.create_all(bind=engine)
    print("Database initialized successfully!")

if __name__ == "__main__":
<<<<<<< HEAD
    init_db()
=======
    init_db()
>>>>>>> 76de304ae82f3cdb583a0ed45183cb1b7af4fe3d
