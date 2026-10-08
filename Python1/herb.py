import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# بارگذاری مدل آموزش دیده
model = load_model('plant_classifier_model.h5')

# تابع پیش‌بینی نوع گیاه
def predict_plant(image_path):
    img_size = 224  # اندازه تصویر ورودی مدل
    datagen = ImageDataGenerator(rescale=1./255)
   
    # بارگذاری تصویر جدید برای پیش‌بینی
    img_array = datagen.flow_from_directory(
        'path_to_your_images',  # مسیر تصاویر ورودی
        target_size=(img_size, img_size),
        class_mode=None,
        batch_size=1,
        shuffle=False)

    predictions = model.predict(img_array)
   
    return predictions

# مثال استفاده
if __name__ == "__main__":
    image_path = input("لطفاً مسیر تصویر گیاه را وارد کنید: ")
   
    result = predict_plant(image_path)
   
    print(f"نتیجه پیش‌بینی: {result}")
 #خراب به هوش مصنوعی ربط می شود نت نیاز دارد