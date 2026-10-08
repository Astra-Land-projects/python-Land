import 'package:flutter/material.dart';

void main() {
  runApp(const MusicApp());
}

class MusicApp extends StatelessWidget {
  const MusicApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Music Player',
      theme: ThemeData(
        useMaterial3: true,
      ),
      home: const MusicPage(),
    );
  }
}

class MusicPage extends StatefulWidget {
  const MusicPage({super.key});

  @override
  State<MusicPage> createState() =>
      _MusicPageState();
}

class _MusicPageState
    extends State<MusicPage> {

  bool playing = false;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title:
            const Text('Music Player'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment:
              MainAxisAlignment.center,
          children: [
            const Icon(
              Icons.album,
              size: 180,
            ),
            const SizedBox(height: 30),
            const Text(
              'My Song',
              style: TextStyle(
                fontSize: 28,
                fontWeight:
                    FontWeight.bold,
              ),
            ),
            const Text(
              'Unknown Artist',
              style: TextStyle(
                fontSize: 18,
              ),
            ),
            const SizedBox(height: 30),
            Slider(
              value: 0.4,
              onChanged: (_) {},
            ),
            IconButton(
              iconSize: 70,
              onPressed: () {
                setState(() {
                  playing = !playing;
                });
              },
              icon: Icon(
                playing
                    ? Icons.pause_circle
                    : Icons.play_circle,
              ),
            ),
          ],
        ),
      ),
    );
  }
}