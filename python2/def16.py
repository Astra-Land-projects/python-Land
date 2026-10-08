def process_signals(signals):
  # استخراج سیگنال‌های بزرگ‌تر مساوی 10
  valid_signals = filter(lambda x: x >= 10, signals)

  # تقویت سیگنال‌های معتبر
  boosted_signals = map(lambda x: x + 2, valid_signals)
 
  return list(boosted_signals)


print(process_signals([10, 5, 6, 7, 8, 15]))
print(process_signals([12, 13, 15, 16, 13]))