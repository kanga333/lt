# lt
application to improve lt

# setup
```bash
python3 -m venv .venv
.venv/bin/activate
pip install -r requirements.txt
```

#### interpreterの設定(Pycharm)
preference  
↓  
Project Interpreter  
↓  
上記で作成した.venv以下を選択

# run
```bash
FLASK_APP=run.py flask db upgrade
python run.py
```
Access to `http://localhost:5000/`
