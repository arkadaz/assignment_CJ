from typing import List

from core.models import Product


class ProductRepository:
    """Repository for product data"""

    @staticmethod
    def get_all_products() -> List[Product]:
        """Get all available products"""
        return [
            Product(
                item_name_thai="นมผงดัดแปลงตราไฮคิว 1 พลัส ซูเปอร์โกลด์",
                item_name_english_approximation="Hi-Q 1 Plus Super Gold Formula",
                promotion_details_thai="ลดสูงสุด 10% (เมื่อซื้อสินค้ากลุ่มนมผงไฮคิวที่ร่วมรายการ)",
                textual_attributes_for_recommendation=["Super Gold", "เสริมธาตุเหล็ก"],
                inferred_color_association_primary="Gold",
            ),
            Product(
                item_name_thai="โฟร์โมสต์ นมยูเอชที",
                item_name_english_approximation="Foremost UHT Milk",
                quantity_size_thai="225 มล. (แพ็ค 6)",
                textual_attributes_for_recommendation=["รสช็อกโกแลต (example flavor)"],
                inferred_color_association_primary="Brown (for chocolate variant)",
            ),
            Product(
                item_name_thai="โอวัลติน ยูเอชที",
                item_name_english_approximation="Ovaltine UHT",
                price_baht=45.00,
                original_price_baht=48.00,
                quantity_size_thai="170/180 มล. (แพ็ค 4)",
                textual_attributes_for_recommendation=["Ovaltine", "Chocolate Malt"],
                inferred_color_association_primary="Orange",
            ),
            Product(
                item_name_thai="ไวตามิ้ลค์ นมถั่วเหลือง ยูเอชที",
                item_name_english_approximation="Vitamilk Soy Milk UHT",
                price_baht=40.00,
                original_price_baht=42.00,
                quantity_size_thai="180 มล. (แพ็ค 3)",
                textual_attributes_for_recommendation=[
                    "Soy",
                    " งาดำและข้าวสีนิล (for To Go variant)",
                ],
                inferred_color_association_primary="Yellow",
            ),
            Product(
                item_name_thai="นมยูเอชที ตราหมีโกลด์",
                item_name_english_approximation="Bear Brand Gold UHT Milk",
                price_baht=69.00,
                original_price_baht=78.00,
                promotion_details_thai="ประหยัด 9.-",
                quantity_size_thai="180 มล. (แพ็ค 4)",
                textual_attributes_for_recommendation=["Gold", "รสจืด (Plain)"],
                inferred_color_association_primary="Gold",
            ),
            Product(
                item_name_thai="ดีน่ากาบา นมถั่วเหลือง",
                item_name_english_approximation="Dna GABA Soy Milk",
                price_baht=225.00,
                original_price_baht=232.00,
                promotion_details_thai="2 คุ้มกว่า",
                quantity_size_thai="จมูกข้าวญี่ปุ่น 1,000 มล. (แพ็คคู่)",
                textual_attributes_for_recommendation=["GABA", "Soy", "จมูกข้าวญี่ปุ่น"],
                inferred_color_association_primary="Green",
            ),
            Product(
                item_name_thai="แอนมัม มาเทอร์น่า นมยูเอชที",
                item_name_english_approximation="Anmum Materna UHT Milk",
                price_baht=350.00,
                promotion_details_thai="ซื้อ 11 ฟรี 1",
                quantity_size_thai="180 มล. (แพ็ค 3) (ซื้อ 12)",
                textual_attributes_for_recommendation=["Materna", "For Mothers"],
                inferred_color_association_primary="Pink",
            ),
            Product(
                item_name_thai="แอนลีน มอฟแม็กซ์ นมยูเอชที",
                item_name_english_approximation="Anlene MovMax UHT Milk",
                price_baht=354.00,
                original_price_baht=399.00,
                promotion_details_thai="ประหยัด 45.-",
                quantity_size_thai="180 มล. (ลัง 4x9)",
                textual_attributes_for_recommendation=["MovMax", "Mobility"],
                inferred_color_association_primary="Blue",
            ),
            Product(
                item_name_thai="เอนชัวร์ โกลด์ แพลนท์เบส กลิ่นอัลมอนด์",
                item_name_english_approximation="Ensure Gold Plant-Based Almond Flavor",
                price_baht=969.00,
                quantity_size_thai="ขนาด 800 กรัม",
                textual_attributes_for_recommendation=[
                    "Ensure Gold",
                    "Plant-Based",
                    "Almond Flavor",
                ],
                inferred_color_association_primary="Green",
            ),
            Product(
                item_name_thai="กลูเซอนา เอสอาร์ ทริปเปิ้ลแคร์",
                item_name_english_approximation="Glucerna SR Triple Care",
                price_baht=685.00,
                original_price_baht=737.00,
                promotion_details_thai="ประหยัด 52.-",
                quantity_size_thai="ขนาด 380 กรัม",
                textual_attributes_for_recommendation=[
                    "Glucerna SR",
                    "Triple Care",
                    "Diabetes Nutrition",
                ],
                inferred_color_association_primary="Blue",
            ),
            Product(
                item_name_thai="โอ๊ตช็อคโก",
                item_name_english_approximation="OAT CHOCO",
                price_baht=26.00,
                original_price_baht=30.00,
                promotion_details_thai="ประหยัด 4.-",
                textual_attributes_for_recommendation=["Oat", "Chocolate"],
                inferred_color_association_primary="Brown",
            ),
            Product(
                item_name_thai="เวสต้า เครื่องดื่มธัญญาหาร",
                item_name_english_approximation="Vesta Cereal Drink",
                price_baht=42.00,
                original_price_baht=45.00,
                promotion_details_thai="ประหยัด 3.-",
                quantity_size_thai="22 กรัม (แพ็ค5)",
                textual_attributes_for_recommendation=[
                    "Cereal",
                    "Strawberry (flavor shown)",
                ],
                inferred_color_association_primary="Red",
            ),
            Product(
                item_name_thai="ไวตามิ้ลค์ ทูโกอินแบล็ค",
                item_name_english_approximation="Vitamilk To Go In Black",
                price_baht=79.00,
                original_price_baht=88.00,
                promotion_details_thai="ประหยัด 9.-",
                quantity_size_thai="300 มล. (แพ็ค 4)",
                textual_attributes_for_recommendation=[
                    "To Go",
                    "In Black",
                    "งาดำ",
                    "ข้าวสีนิล",
                ],
                inferred_color_association_primary="Black",
            ),
        ]
