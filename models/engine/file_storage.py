# """
# FileStorage class that serializes instances to a 
# JSON file and deserializes JSON file to instances"""

# import json
# from models.user import User
# from models.base_model import BaseModel
# from models.state import State
# from models.city import City
# from models.amenity import Amenity
# from models.place import Place
# from models.review import Review

# class FileStorage:
#     """Serializes instances to a JSON file and deserializes JSON file to instances."""

#     __file_path = "storage.json"
#     __objects = {}

#     def all(self, cls=None):
#         """Returns a dictionary of all objects, or filtered by class if cls is provided."""
#         if cls:
#             cls_name = cls.__name__
#             return {key: obj for key, obj in self.__objects.items() if key.startswith(cls_name)}
#         return self.__objects

#     def new(self, obj):
#         """Sets in __objects the obj with key <obj class name>.id."""
#         key = f"{obj.__class__.__name__}.{obj.id}"
#         self.__objects[key] = obj

#     def save(self):
#         """Serializes __objects to the JSON file."""
#         obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
#         with open(self.__file_path, "w", encoding="utf-8") as file:
#             json.dump(obj_dict, file)

#     def reload(self):
#         """Deserializes the JSON file to __objects."""
#         for key, value in self.__objects.items():
#             print(f"Key: {key}, Value: {value}")  # Debugging statement
#             class_name = value['__class__']
#             print(f"Class name: {class_name}")  # Debugging statement
#             class_map = {
#                 'BaseModel': BaseModel,
#                 'User': User,
#                 'State': State,
#                 'City': City,
#                 'Amenity': Amenity,
#                 'Place': Place,
#                 'Review': Review
#             }
#             if class_name in class_map:
#                 self.__objects[key] = class_map[class_name](**value)
#             else:
#                 print(f"Class {class_name} not found in class_map")

#     def delete(self, obj=None):
#         """Deletes obj from __objects if it exists."""
#         if obj is not None:
#             key = f"{obj.__class__.__name__}.{obj.id}"
#             if key in self.__objects:
#                 del self.__objects[key]
#                 self.save()

   


"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            return {k: v for k, v in FileStorage.__objects.items()
                    if isinstance(v, cls)}
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete obj from __objects if it’s inside"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            del self.all()[key]
            self.save()