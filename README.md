## Yapay Zekâ Destekli İşe Alım Değerlendirme Sistemi

Bu proje, işe alım süreçlerinde başvuran adayları belirli kriterlere göre değerlendirerek yapay zekâ destekli bir karar mekanizması sunar.
Flask ile geliştirilen bu web uygulaması, adayın eğitim düzeyi, deneyim süresi, yetenekleri, proje geçmişi gibi bilgileri alır ve bir makine öğrenmesi modeli yardımıyla adayın uygunluğunu değerlendirir.


## Proje Amacı

Günümüzde insan kaynakları birimlerinde işe alım süreci oldukça zaman alıcıdır. Bu projeyle amaçlanan:
- Aday değerlendirmesini hızlı ve objektif hâle getirmek,
- Ön eleme sürecini otomatikleştirerek İK ekiplerinin yükünü azaltmak,
- Adaylara geri bildirim sağlamak.


## Kullanılan Teknolojiler

- **Python**
- **Flask** – Web sunucusu
- **HTML / CSS** – Arayüz
- **scikit-learn** – Makine öğrenmesi modeli
- **Pandas / NumPy** – Veri işlemleri

---

## Form Girdileri

Kullanıcıdan alınan bilgiler:

- **Eğitim Durumu:** (Ön Lisans, Lisans, Yüksek Lisans)
- **Deneyim (yıl):**
- **Sertifika:** (Evet / Hayır)
- **Yetenekler:**
  - Python, Java, SQL, Machine Learning, Veri Analizi, İletişim
- **Proje Sayısı**
- **Pozisyon:** (Veri Analisti, Yazılım Geliştirici vb.)
- **Maaş Beklentisi ($)**

