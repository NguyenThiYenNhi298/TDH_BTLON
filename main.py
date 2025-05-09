import time
import schedule
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def lay_tin_vnexpress():
    print("Bắt đầu lấy tin từ VnExpress...")
    driver = webdriver.Chrome()
    data = []
    count_page = 0
    max_page = 1  

    while True:
        count_page += 1
        if count_page > max_page:
            print(f" Đã lấy số trnag là {max_page} trang")
            break

        url = f"https://vnexpress.net/cong-nghe-p{count_page}"
        print(f"Đang lấy dữ liệu trang số {count_page}...")

        driver.get(url)

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".title-news a"))
            )
        except:
            print(f"Trang {count_page} không tải được. Dừng.")
            break

        tin_list = driver.find_elements(By.CSS_SELECTOR, ".title-news a")

        if not tin_list:
            print("Đã hét tin để lấy")
            break

        for tin in tin_list:
            try:
                tieude = tin.text.strip()
                link_baiviet = tin.get_attribute("href")

                driver.execute_script("window.open()")
                driver.switch_to.window(driver.window_handles[1])
                driver.get(link_baiviet)
                time.sleep(2)

                try:
                    mota = driver.find_element(By.CSS_SELECTOR, "meta[name='description']").get_attribute("content")
                except:
                    mota = "Không có mô tả"

                try:
                    hinh = driver.find_element(By.CSS_SELECTOR, ".fig-picture picture img")
                    hinh_url = hinh.get_attribute("src")
                except:
                    hinh_url = "Không có hình ảnh"

                try:
                    nd_list = driver.find_elements(By.CSS_SELECTOR, ".fck_detail p")
                    noidung = "\n".join([p.text for p in nd_list if p.text.strip()])
                except:
                    noidung = "Không lấy được nội dung"

                driver.close()
                driver.switch_to.window(driver.window_handles[0])

                data.append({
                    "tieude": tieude,
                    "mota": mota,
                    "hinhanh": hinh_url,
                    "noidung": noidung
                })
                print(f"✔ {tieude}")

            except:
                print("Lỗi khi lấy tin.")
                if len(driver.window_handles) > 1:
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])

    driver.quit()

    # Lưu vào Excel
    df = pd.DataFrame(data)
    df.to_excel("TinTuc_VnExpress.xlsx", index=False)
    print(" Đã lưu dữ liệu vào file Excel")

# Lên lịch chạy lúc 6h sáng (đổi thành giờ test nếu cần)
schedule.every().day.at("14:46").do(lay_tin_vnexpress)

print(" Đang chờ đến giờ để chạy")

while True:
    schedule.run_pending()
    time.sleep(60)
