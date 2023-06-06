from ..config.database import Database
from ..config.settings import settings


class SearchController:
    @staticmethod
    def get_search(property_filters, status_history_filters, status_filter) -> list:
        if property_filters:
            address_filter = property_filters.get("address")
            city_filter = property_filters.get("city")
            price_min_filter = property_filters.get("price_min")
            price_max_filter = property_filters.get("price_max")
            year_filter = property_filters.get("year")

        if status_history_filters:
            update_date_filter = status_history_filters.get("update_date")

        if status_filter:
            name_filter = status_filter.get("name")
            label_filter = status_filter.get("label")

        db_connection = Database(settings=settings.serialize())
        db_connection.connect()
        cursor = db_connection.connection.cursor()

        params = {
            "address": address_filter,
            "city": city_filter,
            "price_min": price_min_filter,
            "price_max": price_max_filter,
            "year": year_filter,
            "update_date": update_date_filter,
            "status_name": name_filter,
            "status_label": label_filter,
        }

        query = (
            "SELECT p.id, p.address, p.city, p.price, p.description, p.year, s.name, s.label, sh.update_date"
            " FROM property AS p INNER JOIN status_history AS sh ON p.id = sh.property_id INNER JOIN"
            " status AS s ON sh.status_id = s.id WHERE 1 = 1"
        )

        conditions = []
        params_values = {}

        if params["address"]:
            conditions.append("p.address = %(address)s")
            params_values["address"] = params["address"]

        if params["city"]:
            conditions.append("p.city = %(city)s")
            params_values["city"] = params["city"]

        if params["price_min"]:
            conditions.append("p.price >= %(price_min)s")
            params_values["price_min"] = params["price_min"]

        if params["price_max"]:
            conditions.append("p.price <= %(price_max)s")
            params_values["price_max"] = params["price_max"]

        if params["year"]:
            conditions.append("p.year = %(year)s")
            params_values["year"] = params["year"]

        if params["update_date"]:
            conditions.append("DATE(sh.update_date) = DATE(%(update_date)s)")
            params_values["update_date"] = params["update_date"]

        if params["status_name"]:
            conditions.append("s.name = %(status_name)s")
            params_values["status_name"] = params["status_name"]

        if params["status_label"]:
            conditions.append("s.label = %(status_label)s")
            params_values["status_label"] = params["status_label"]

        if conditions:
            query += " AND " + " AND ".join(conditions)

        cursor.execute(query, params_values)

        results_db = cursor.fetchall()
        results_dict = [
            dict(
                zip(
                    [
                        "id_property",
                        "address",
                        "city",
                        "price",
                        "description",
                        "year",
                        "status_name",
                        "status_label",
                        "update_date",
                    ],
                    row,
                )
            )
            for row in results_db
        ]

        cursor.close()
        db_connection.disconnect()

        return results_dict
