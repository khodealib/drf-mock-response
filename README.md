# drf-mock-response

📦 A lightweight mock response framework for Django REST Framework (DRF).  
Easily simulate API endpoints using static JSON files stored inside your Django apps.

---

## 🔧 Features

-   Plug & play mock API views (List, Detail, Update, Delete)
-   Supports `ViewSet`-based mocks
-   Loads JSON mock data from `json_mock/` directory inside each Django app
-   Customizable HTTP status code and response delay
-   No real DB or models required

---

## 📁 Project Structure

In each Django app:

```
your_app/
├── json_mock/
│ └── your_mock.json
├── views/
│ └── your_mock_views.py

```

---

## 🚀 Installation

```bash
pip install git+https://github.com/yourusername/drf-mock-response.git
```

Or after cloning:

```
pip install /path/to/drf_mock_response/
```

## 🧩 Usage

```python
# your_app/views/mocks.py

from drf_mock_response.views import MockListAPIView

class ProductListMock(MockListAPIView):
    json_filename = "product_list.json"
    mock_status = 200
    delay_seconds = 1
```

```python
# your_app/urls.py

from django.urls import path
from .views.mocks import ProductListMock

urlpatterns = [
    path("mock/products/", ProductListMock.as_view()),
]
```

Place your mock file in:

```
your_app/json_mock/product_list.json

```

### 🔁 ViewSet Example

```python
from drf_mock_response.viewsets import MockViewSet

class UserMockViewSet(MockViewSet):
    json_filename = "user_list.json"
```

And wire it with a router in your urls.py.

## ✅ Requirements

    Django ≥ 3.2
    djangorestframework ≥ 3.14

## 📄 License

MIT © 2025 Ali Bagheri
