# Gerenciador de Senhas

## Introdução

Este Gerenciador de Senhas foi criado por **Mizael Junior** em setembro de 2024 como parte de seu primeiro projeto externo. Durante o desenvolvimento, utilizei diferentes tecnologias e retirei dúvidas ao longo do processo, aprendendo novas abordagens e técnicas em Python. Embora o projeto tenha sido idealizado por mim, parte de seu desenvolvimento contou com apoio de fontes externas, tornando-o uma excelente ferramenta de estudo e compreensão da programação em Python.

---

## Funcionalidades

- **Cadastro de Senhas**: Permite que o usuário registre novas senhas associadas a sites e nomes de usuários.
- **Leitura de Senhas**: O sistema exibe todas as senhas já cadastradas.
- **Exclusão de Senhas**: Permite deletar entradas existentes no banco de dados.
- **Login Simples**: Requer um login para acessar as funcionalidades do gerenciador.

---

## Informações Técnicas

Este projeto utiliza a linguagem **Python** e suas bibliotecas padrão, sem dependências externas. O código foi organizado de maneira modular para facilitar sua manutenção e leitura.

- **Sistema de Login**: O sistema requer um usuário e uma senha para acessar o gerenciador de senhas. No momento, há apenas um usuário e senha disponíveis:
  - **Usuário**: `main`
  - **Senha**: `123`
  
- **Gerador de IDs**: Cada nova senha cadastrada recebe um ID único gerado automaticamente.
  
- **Armazenamento**: As senhas são armazenadas em um arquivo de texto no formato `ID;SITE;USUÁRIO;SENHA`.

---

## Como Usar

1. Faça o clone ou download deste repositório.
   
   ```bash
   git clone https://github.com/mizaeljunior0r/ProjetoBancosenhasimples.git
   cd ProjetoBancosenhasimples
