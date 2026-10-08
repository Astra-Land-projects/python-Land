import 'package:flutter/material.dart';

void main() {
  runApp(const ExpenseApp());
}

class ExpenseApp extends StatelessWidget {
  const ExpenseApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Expense Tracker',
      theme: ThemeData(
        useMaterial3: true,
      ),
      home: const ExpensePage(),
    );
  }
}

class ExpensePage extends StatefulWidget {
  const ExpensePage({super.key});

  @override
  State<ExpensePage> createState() =>
      _ExpensePageState();
}

class _ExpensePageState
    extends State<ExpensePage> {

  final List<Map<String, dynamic>>
      expenses = [];

  final titleController =
      TextEditingController();

  final amountController =
      TextEditingController();

  void addExpense() {

    final title =
        titleController.text.trim();

    final amount =
        double.tryParse(
      amountController.text,
    );

    if (
      title.isEmpty ||
      amount == null
    ) {
      return;
    }

    setState(() {

      expenses.add({
        'title': title,
        'amount': amount,
      });

      titleController.clear();
      amountController.clear();
    });
  }

  double get total {

    return expenses.fold(
      0.0,
      (sum, item) =>
          sum + item['amount'],
    );
  }

  @override
  Widget build(BuildContext context) {

    return Scaffold(
      appBar: AppBar(
        title:
            const Text('Expenses'),
      ),
      body: Column(
        children: [

          Card(
            margin:
                const EdgeInsets.all(16),
            child: Padding(
              padding:
                  const EdgeInsets.all(16),
              child: Column(
                children: [

                  const Text(
                    'Total Expenses',
                    style:
                        TextStyle(
                      fontSize: 18,
                    ),
                  ),

                  Text(
                    '\$${total.toStringAsFixed(2)}',
                    style:
                        const TextStyle(
                      fontSize: 32,
                      fontWeight:
                          FontWeight.bold,
                    ),
                  ),

                  TextField(
                    controller:
                        titleController,
                    decoration:
                        const InputDecoration(
                      labelText: 'Title',
                    ),
                  ),

                  TextField(
                    controller:
                        amountController,
                    keyboardType:
                        TextInputType.number,
                    decoration:
                        const InputDecoration(
                      labelText: 'Amount',
                    ),
                  ),

                  const SizedBox(
                    height: 10,
                  ),

                  ElevatedButton(
                    onPressed: addExpense,
                    child:
                        const Text('Add'),
                  ),
                ],
              ),
            ),
          ),

          Expanded(
            child:
                ListView.builder(
              itemCount:
                  expenses.length,
              itemBuilder:
                  (context, index) {

                final expense =
                    expenses[index];

                return ListTile(
                  title:
                      Text(expense['title']),
                  trailing:
                      Text(
                    '\$${expense['amount'].toStringAsFixed(2)}',
                  ),
                );
              },
            ),
          ),
        ],
      ),
    );
  }
}