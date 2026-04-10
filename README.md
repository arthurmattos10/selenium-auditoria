# 🤖 Robô de Auditoria Multitarefa com Selenium

## 📚 Sobre o Projeto

Este projeto foi desenvolvido como atividade prática da disciplina **Automação de Testes de Software**, cursada no **5º semestre** da graduação na Faculdade Impacta.

O objetivo foi criar um script automatizado utilizando **Selenium WebDriver**, capaz de operar em modo headless, gerenciar múltiplas abas, interagir com elementos dinâmicos e extrair dados da web.

---

## 🚀 Tecnologias Utilizadas

* Python
* Selenium WebDriver
* WebDriver Manager
* Google Chrome (modo headless)

---

## 🎯 Objetivo do Projeto

Desenvolver um robô de auditoria que:

* Execute sem interface gráfica (modo headless)
* Gerencie múltiplas abas simultaneamente
* Utilize esperas implícitas e explícitas
* Interaja com elementos dinâmicos
* Extraia informações da web
* Gere evidências (screenshot)

---

## ⚙️ Funcionalidades Implementadas

### 🔹 Parte 1 – Configuração Inicial

* Execução em modo headless
* Definição de resolução (1920x1080)
* Configuração de espera implícita

---

### 🔹 Parte 2 – Múltiplas Abas

* Abertura de novas abas com `window.open()`
* Controle de abas com `window_handles`
* Validação da abertura de novas janelas

---

### 🔹 Parte 3 – Interação com Dropdown

* Seleção de opções com a classe `Select`
* Validação do valor selecionado

---

### 🔹 Parte 4 – Espera Explícita

* Uso de `WebDriverWait`
* Sincronização com conteúdo dinâmico
* Extração de texto após carregamento

---

### 🔹 Parte 5 – Extração de Dados

* Interação com a Wikipédia
* Preenchimento de campo de busca
* Extração de texto e atributo (`href`)
* Geração de evidência com screenshot

---

### 🔹 Parte 6 – Encerramento

* Finalização correta do navegador com `driver.quit()`

---

## 🖥️ Como Executar o Projeto

### 1. Instalar dependências

```bash
pip install selenium
pip install webdriver-manager
```

### 2. Executar o script

```bash
python robo_auditoria_selenium.py
```

---

## 📸 Evidência Gerada

O script gera automaticamente um arquivo:

```
evidencia_wiki.png
```

Comprovando a execução da automação.

---

## 🧠 Conceitos Aplicados

* Automação de testes web
* Manipulação de DOM
* Sincronização de testes
* Testes headless
* Web scraping básico
* Boas práticas com Selenium

---

## 📌 Observações

Este projeto tem caráter acadêmico e foi desenvolvido com foco no aprendizado prático de automação de testes, simulando cenários reais de execução em ambiente de servidor.

---

## 👨‍💻 Autor

Desenvolvido por mim **Arthur Matos Rocha**
Estudante de Análise e Desenvolvimento de Sistemas
Faculdade Impacta
