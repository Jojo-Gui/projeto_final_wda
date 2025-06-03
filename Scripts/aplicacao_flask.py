from flask import Flask, jsonify
import pandas as pd
import json

app = Flask(__name__)

@app.route('/')
def oi():
        return 'Sandálias de qualidade e com o melhor preço, vocÊ encontra na Lolita Pimentoa!'
@app.route('/dados')
def carregardado():
        df = pd.read_csv('Base_Tratada/produtos_lolita_pimenta_tratados.csv', sep=';', encoding='utf-8')
        df.sort_values(by='desconto').head(10)
        return jsonify(df.to_json())

if __name__ == '__main__':
        app.run(debug=True)