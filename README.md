# Installationshinweise 

Einrichtung eines Streamlit Dashboards mit OpenAI Assistants API als Docker-Container in der BW-Cloud und Bereitstellung auf einer https-Adresse.

### Streamlit und Docker

[Streamlit mit Docker in der BW-Cloud aufsetzen](https://docs.streamlit.io/knowledge-base/tutorials/deploy/docker)

### Reverse Proxy

- Nginx installieren: Führen Sie auf Ihrem Server `sudo apt update` und dann `sudo apt install nginx` aus, um Nginx zu installieren.

- Öffnen Sie die Konfigurationsfile in /etc/nginx/sites-available/. Sie können dies mit einem Texteditor wie nano oder vim tun:

```
sudo nano /etc/nginx/sites-available/default
```

- Den Inhalt mit diesem Code ersetzen:

```perl
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    server_name _;

    location / {
        proxy_pass http://localhost:8501;  # Port des ersten Streamlit-Dashboards
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}

# Optional, falls weitere Dashboards benötigt werden
server {
    listen 81;  # Alternativer Port für das zweite Dashboard
    listen [::]:81;
    server_name _;

    location / {
        proxy_pass http://localhost:8502;  # Port des zweiten Streamlit-Dashboards
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}

```

- Speichern und Testen der Konfiguration: Speichern Sie die Datei nach den Änderungen und führen Sie `sudo nginx -t` aus, um sicherzustellen, dass keine Syntaxfehler vorliegen.


- Nginx neustarten: Starten Sie Nginx neu, um die Änderungen zu übernehmen:

```bash
sudo systemctl restart nginx
```

- Firewall anpassen (falls erforderlich): Wenn Sie eine Firewall wie UFW verwenden, erlauben Sie den HTTP-Verkehr:

```bash
sudo ufw allow 'Nginx Full'
```

## Docker starten

Dashoboard erstellen

```bash
sudo docker build -t docker-gpt .
```

Dashboard 1 (streamlit):

```bash
sudo docker run -p 8501:8501 streamlit
```

Dashboard 2:

```bash
sudo docker run -p 8502:8501 <IhrDockerImage>
```

## Https

Https-Zertifikat beantragen für BW-Cloud .org Adresse  (Nginx auf Ubuntu):

- [certbot instructions](https://certbot.eff.org/instructions?ws=nginx&os=ubuntufocal)

