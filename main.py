from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Calculadora DZX-CORE - Deploy Real</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            margin: 0;
            padding: 20px;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            max-width: 400px;
            width: 100%;
            text-align: center;
        }
        h1 {
            color: #333;
            margin-bottom: 20px;
        }
        .status {
            background: #4CAF50;
            color: white;
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 20px;
            font-weight: bold;
        }
        input {
            width: 90%;
            padding: 12px;
            margin: 8px 0;
            border: 2px solid #ddd;
            border-radius: 5px;
            font-size: 16px;
        }
        .buttons {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            margin: 20px 0;
        }
        button {
            padding: 15px;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            background: #4CAF50;
            color: white;
            transition: background 0.3s;
        }
        button:hover {
            background: #45a049;
        }
        #resultado {
            background: #f0f0f0;
            padding: 15px;
            border-radius: 5px;
            margin: 15px 0;
            min-height: 30px;
            font-size: 18px;
            font-weight: bold;
        }
        .footer {
            margin-top: 20px;
            color: #666;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Calculadora Web</h1>
        <div class="status">Deploy Real Funcionando!</div>
        
        <input type="number" id="num1" placeholder="Primeiro número" step="any">
        <input type="number" id="num2" placeholder="Segundo número" step="any">
        
        <div class="buttons">
            <button onclick="calcular('+'))">+ Somar</button>
            <button onclick="calcular('-'))">- Subtrair</button>
            <button onclick="calcular('*'))">× Multiplicar</button>
            <button onclick="calcular('/'))">÷ Dividir</button>
        </div>
        
        <div id="resultado">Digite os números e clique em uma operação</div>
        
        <div class="footer">
            Criado pelo orquestrador DZX-CORE<br>
            Deploy automático confirmado
        </div>
    </div>
    
    <script>
        function calcular(operacao) {
            const num1 = parseFloat(document.getElementById('num1').value);
            const num2 = parseFloat(document.getElementById('num2').value);
            
            if (isNaN(num1) || isNaN(num2)) {
                document.getElementById('resultado').innerHTML = 'Por favor, digite números válidos';
                return;
            }
            
            let resultado;
            let simbolo = operacao;
            
            switch(operacao) {
                case '+':
                    resultado = num1 + num2;
                    break;
                case '-':
                    resultado = num1 - num2;
                    break;
                case '*':
                    resultado = num1 * num2;
                    simbolo = '×';
                    break;
                case '/':
                    if (num2 === 0) {
                        document.getElementById('resultado').innerHTML = 'Erro: Não é possível dividir por zero';
                        return;
                    }
                    resultado = num1 / num2;
                    simbolo = '÷';
                    break;
            }
            
            document.getElementById('resultado').innerHTML = 
                num1 + ' ' + simbolo + ' ' + num2 + ' = ' + resultado.toFixed(2).replace(/\.?0+$/, '');
        }
        
        // Testar se JavaScript está funcionando
        document.addEventListener('DOMContentLoaded', function() {
            console.log('Calculadora carregada com sucesso!');
        });
    </script>
</body>
</html>
"""

@app.route("/health")
def health():
    return {"status": "ok", "message": "Aplicacao funcionando", "deploy": "real"}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
