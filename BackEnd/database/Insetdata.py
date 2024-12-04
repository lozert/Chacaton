from database.config import cursor, conn

def insert_title_type(title):
    insert_query = "INSERT INTO title_type (title) VALUES (%s);"

    cursor.execute(insert_query, (title,))
    conn.commit()

def insert_data(title: int, text: str, keywords: list):
    insert_query = "INSERT INTO data (title, text, keywords) VALUES (%s, %s, %s);"

    cursor.execute(insert_query, (title, text, keywords))
    conn.commit()

# title = ["Защита растений", "Почвоведение и питание растений", "Агроклиматические условия"]

# for item in title:
#     insert_title_type(item)


if __name__ == "__main__":
    text = "Зоны рискованного земледелия — это территории, где климатические или природные условия создают значительные риски для успешного сельскохозяйственного производства. Эти зоны характеризуются нестабильными климатическими условиями, такими как недостаток или избыток влаги, частые заморозки, высокие температуры, сильные ветры или недостаточная солнечная радиация. Рискованное земледелие требует применения специальных агротехнических мероприятий, таких как выбор устойчивых к климатическим факторам сортов растений, орошение или защита от заморозков. Такие зоны часто нуждаются в дополнительных усилиях для стабилизации урожайности и защиты от природных катастроф."

    keywords = ["рискованное земледелие", "климатические условия", "агротехнические мероприятия", "засухи", "заморозки"]
    insert_data(3, text=text, keywords=keywords)