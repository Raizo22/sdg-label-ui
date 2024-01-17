def create_html_page():
    html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Judul Halaman</title>
    <style>
        /* Gaya CSS */
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f0f0f0;
            color: #333;
            display: flex;
            flex-direction: column;
            align-items: center;
            min-height: 100vh;
        }

        header, footer {
            background-color: #333;
            color: #fff;
            padding: 20px 0;
            text-align: center;
            width: 100%;
        }

        main {
            flex: 1;
            padding: 20px;
            text-align: center;
            width: 80%;
        }

        .frame {
            border: 1px solid #ccc;
            padding: 20px;
            border-radius: 8px;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            width: 100%;
            align-items: start;
        }

        button {
            margin: 10px;
            padding: 12px 24px;
            border: 2px solid #333;
            border-radius: 8px;
            width: calc(100% - 24px);
            box-sizing: border-box;
            background-color: #333;
            color: #fff;
            cursor: pointer;
            transition: background-color 0.3s ease;
            font-size: 16px;
        }

        button:hover {
            background-color: #555;
        }

        textarea {
            resize: none;
            width: 100%;
            height: 120px;
            overflow-y: scroll;
            border-radius: 8px;
            border: 2px solid #ccc;
            padding: 12px;
            font-size: 14px;
        }

        .grid-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }

        .grid-item {
            border: 1px solid #ccc;
            border-radius: 8px;
            padding: 10px;
            text-align: left;
            word-wrap: break-word;
            width: 100%;
        }

        .output-container {
            border: 1px solid #ccc;
            border-radius: 8px;
            padding: 10px;
            text-align: left;
            word-wrap: break-word;
            width: 100%;
        }

        .notification {
            background-color: #4CAF50;
            color: white;
            text-align: center;
            padding: 12px;
            margin-top: 20px;
            display: none;
            border-radius: 8px;
        }
    </style>
</head>
<body>

    <!-- Bagian Header -->
    <header>
        <h1 style="margin: 0;">Sgd Labels</h1>
    </header>

    <!-- Bagian Body -->
    <main>
        <div class="frame">
            <button onclick="changeContent('text')">Input Teks</button>
            <button onclick="changeContent('file')">Input File</button>
            <div id="text-input" style="display: none; grid-column: span 2;">
                <div class="grid-item">
                    <textarea id="input-text" placeholder="Masukkan teks" oninput="autoResize(this)"></textarea>
                    <button onclick="submitText()">Submit</button>
                </div>
            </div>
            <div id="file-input" style="display: none; grid-column: span 2;">
                <div class="grid-item">
                    <label for="file-upload" class="custom-file-upload">
                        Upload File CSV
                    </label>
                    <input id="file-upload" type="file" accept=".csv" onchange="submitFile(this)">
                </div>
            </div>
        </div>
        <div class="grid-container" id="content">
            <!-- Tempat untuk menampilkan output hasil -->
            <div class="output-container" id="output"></div>
        </div>
        <div class="notification" id="success-msg"></div>
    </main>

    <!-- Bagian Footer -->
    <footer>
        <p style="margin: 0;">Footer - Hak Cipta &copy; 2024</p>
    </footer>

    <script>
        function changeContent(option) {
            var textInput = document.getElementById('text-input');
            var fileInput = document.getElementById('file-input');
            textInput.style.display = option === 'text' ? 'grid' : 'none';
            fileInput.style.display = option === 'file' ? 'grid' : 'none';
        }

        function autoResize(textarea) {
            textarea.style.height = 'auto';
            textarea.style.height = (textarea.scrollHeight) + 'px';
        }

        function submitText() {
            var inputText = document.getElementById('input-text');
            var contentDiv = document.getElementById('output');
            var text = inputText.value.trim();

            // Check if the entered text has at least 50 words
            var wordCount = text.split(/\s+/).length;
            if (wordCount < 50) {
                document.getElementById('success-msg').style.display = 'none';
                contentDiv.innerHTML = '<div class="grid-item"><p>Masukkan minimal 50 kata.</p></div>';
            } else {
                // Display success message
                document.getElementById('success-msg').style.display = 'block';
                document.getElementById('success-msg').innerHTML = 'Data teks berhasil di-submit dan ditampilkan dalam grid.';
                contentDiv.innerHTML = '<div class="output-container"><p>Data hasil output:</p>' + text + '</div>';
            }
        }

        function submitFile(input) {
            var file = input.files[0];
            var contentDiv = document.getElementById('output');
            var reader = new FileReader();
            reader.onload = function(event) {
                var csv = event.target.result;
                // Lakukan manipulasi CSV jika diperlukan
                document.getElementById('success-msg').style.display = 'block';
                document.getElementById('success-msg').innerHTML = 'File CSV berhasil diunggah.';
                contentDiv.innerHTML = '<div class="output-container"><p>Data hasil output:</p>' + csv + '</div>';
            };
            reader.readAsText(file);
        }
    </script>

</body>
</html>


'''

    # Menyimpan konten HTML ke dalam file
    with open('halaman.html', 'w') as file:
        file.write(html_content)

    # Membuka file HTML di browser
    import webbrowser
    webbrowser.open('halaman.html')

if __name__ == '__main__':
    create_html_page()
