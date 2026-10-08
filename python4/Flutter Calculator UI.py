import 'package:flutter/material.dart';

void main() {
  runApp(const CalculatorApp());
}

class CalculatorApp extends StatelessWidget {
  const CalculatorApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Calculator',
      theme: ThemeData(
        useMaterial3: true,
      ),
      home: const CalculatorPage(),
    );
  }
}

class CalculatorPage extends StatefulWidget {
  const CalculatorPage({super.key});

  @override
  State<CalculatorPage> createState() =>
      _CalculatorPageState();
}

class _CalculatorPageState
    extends State<CalculatorPage> {

  String display = '0';

  void press(String value) {
    setState(() {

      if (value == 'C') {
        display = '0';
        return;
      }

      if (display == '0') {
        display = value;
      } else {
        display += value;
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    final buttons = [
      '7', '8', '9', '/',
      '4', '5', '6', '*',
      '1', '2', '3', '-',
      '0', 'C', '=', '+',
    ];

    return Scaffold(
      appBar: AppBar(
        title: const Text('Calculator'),
      ),
      body: Column(
        children: [
          Expanded(
            child: Container(
              alignment:
                  Alignment.bottomRight,
              padding:
                  const EdgeInsets.all(24),
              child: Text(
                display,
                style: const TextStyle(
                  fontSize: 40,
                ),
              ),
            ),
          ),
          Expanded(
            flex: 2,
            child: GridView.count(
              crossAxisCount: 4,
              padding:
                  const EdgeInsets.all(8),
              children: buttons.map(
                (button) {
                  return Padding(
                    padding:
                        const EdgeInsets.all(4),
                    child: ElevatedButton(
                      onPressed: () {
                        press(button);
                      },
                      child: Text(
                        button,
                        style:
                            const TextStyle(
                          fontSize: 24,
                        ),
                      ),
                    ),
                  );
                },
              ).toList(),
            ),
          ),
        ],
      ),
    );
  }
}