import 'package:flutter/material.dart';

void main() => runApp(const CurrencyApp());

class CurrencyApp extends StatelessWidget {
  const CurrencyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(useMaterial3: true),
      home: const CurrencyPage(),
    );
  }
}

class CurrencyPage extends StatefulWidget {
  const CurrencyPage({super.key});

  @override
  State<CurrencyPage> createState() =>
      _CurrencyPageState();
}

class _CurrencyPageState
    extends State<CurrencyPage> {

  final controller = TextEditingController();

  double result = 0;

  void convert() {
    final value =
        double.tryParse(controller.text) ?? 0;

    setState(() {
      result = value * 0.92;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Currency Converter"),
      ),
      body: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          children: [
            TextField(
              controller: controller,
              keyboardType:
                  TextInputType.number,
              decoration: const InputDecoration(
                labelText: "EUR",
                border: OutlineInputBorder(),
              ),
            ),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: convert,
              child: const Text("Convert"),
            ),
            const SizedBox(height: 20),
            Text(
              "\$${result.toStringAsFixed(2)}",
              style: const TextStyle(
                fontSize: 32,
              ),
            ),
          ],
        ),
      ),
    );
  }
}