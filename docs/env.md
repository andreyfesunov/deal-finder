# Environment Variables

## About

Environment variables are used to configure the application.
The application requires the following environment variables:

- `CATEGORIES_CSV_FILE_PATH`: Path to the CSV file containing product category data. This file should contain category and subcategory information used for organizing products. Default: "data/categories.csv"

- `PRODUCTS_CSV_FILE_PATH`: Path to the CSV file containing product data. This file stores product details including names, prices and links from different retailers (M.Video, Eldorado, DNS, Citilink, Yandex Market). Default: "data/products.csv"

## Usage

1. Create a `.env` file in the root directory.
2. Add the environment variables to the `.env` file.
3. Run the application.
