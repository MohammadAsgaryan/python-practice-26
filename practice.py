def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("❌ خطا: تقسیم بر صفر امکان‌پذیر نیست!")
        return None


while True:
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        break
    except ValueError:
        print("❌ ورودی نامعتبر! لطفاً فقط عدد وارد کنید.\n")


result = divide(num1, num2)

if result is not None:
    print("✅ Result:", result)

print("🎯 برنامه با موفقیت اجرا شد!")
