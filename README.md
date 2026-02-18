# Car Management API

This is a simple Django REST Framework API for managing cars, people, and firms (companies). It provides endpoints to create, retrieve, and potentially update data related to these entities.

## Overview

The application consists of:

*   **models.py:** Defines the database models for `Person`, `Firm` (Company), and `Car`.
*   **urls.py:** Configures the URL patterns for the API endpoints.
*   **serializers.py:**  Handles data serialization and deserialization between Python objects and JSON format, used by Django REST Framework.
*   **views.py:** Contains the actual API view functions that handle requests and interact with the models and serializers.

## Models

The following database tables are defined:

*   **Person:** Stores information about individuals (owners of cars).
    *   `name`:  String representing the person's name.
    *   `moobile`: Integer representing a mobile phone number.
    *   `date`: Datetime field, automatically set to the time of creation.

*   **Firm:** Stores information about companies (owners or associated with cars).
    *   `title`: String representing the company's title/name.
    *   `membership_code`: Integer representing a unique membership code for the firm.

*   **Car:**  Stores information about vehicles.
    *   `company`: String representing the car manufacturer (e.g., "Toyota", "BMW").
    *   `price`: Integer representing the price of the car.
    *   `owner`: Foreign key referencing the `Person` model, indicating who owns the car.  Deleting a person will cascade delete their cars.
    *   `store`: Foreign key referencing the `Firm` model, allowing a company to be associated with a car (optional). Deleting a firm will cascade delete its cars.

## API Endpoints

| Endpoint      | Method | Description                               | Request Body Example          | Response Status Code |
|---------------|--------|-------------------------------------------|-------------------------------|----------------------|
| `/pr`         | GET    | Retrieve all Persons                        | None                          | 200 OK                |
| `/pr`         | POST   | Create a new Person                         | `{"name": "John Doe", "moobile": 123}` | 201 Created           |
| `/cr`         | GET    | Retrieve all Cars                           | None                          | 200 OK                |
| `/cr`         | POST   | Create a new Car                            | `{"company": "Toyota", "price": 25000}` | 201 Created           |
| `/info`       | GET    | Retrieve all Cars                           | None                          | 200 OK                |
| `/add_frim`   | POST   | Create a new Firm                            | `{"title": "Acme Corp"}`        | 201 Created           |

## Serializers

The serializers are used to convert between Python objects and JSON for the API.  They are defined in `serializers.py`.

*   `per_ser`: Serializer for the `Person` model.
*   `car_ser`: Serializer for the `Car` model.
*   `infouw`: Serializer for the `Car` model (used with nested relationships).
*   `frim_ser`: Serializer for the `Firm` model.
*   `inpho`: Serializer for the `Firm` model.

## Usage Notes

*   This is a basic API and doesn't include features like authentication, pagination, or error handling beyond what Django REST Framework provides.
*   The database setup would need to be configured separately (e.g., using Django migrations).
*   Consider adding more robust validation and error handling for production use.

## Further Development Ideas

*   Implement user authentication and authorization.
*   Add pagination to handle large datasets.
*   Implement input validation and error handling.
*   Extend the API with additional features (e.g., car search, filtering).
