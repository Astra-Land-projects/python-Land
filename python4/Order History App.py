import 'package:flutter/material.dart';

void main() => runApp(const OrdersApp());

class OrdersApp extends StatelessWidget {
  const OrdersApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(useMaterial3: true),
      home: Scaffold(
        appBar: AppBar(title: const Text("Orders")),
        body: ListView(
          children: const [
            ListTile(title: Text("Order #1"), subtitle: Text("Delivered")),
            ListTile(title: Text("Order #2"), subtitle: Text("On the way")),
            ListTile(title: Text("Order #3"), subtitle: Text("Cancelled")),
          ],
        ),
      ),
    );
  }
}