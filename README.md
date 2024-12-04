# Gerador de Senhas Aleatórias

## Objetivos do Projeto

O objetivo deste projeto é desenvolver um gerador de senhas aleatórias em Python, com funcionalidades flexíveis para permitir a personalização da senha gerada conforme as necessidades do usuário. A ferramenta permitirá que o usuário configure o comprimento da senha, escolha se deseja incluir letras maiúsculas, números e caracteres especiais (símbolos), criando senhas seguras e variadas.

## Funcionalidades que Serão Implementadas

1. **Geração de Senha Aleatória**:
   - O sistema deve gerar senhas aleatórias com base nas opções fornecidas pelo usuário.

2. **Configuração de Comprimento**:
   - O usuário poderá definir o comprimento da senha (com limite máximo de 15 caracteres).

3. **Opção para Incluir Letras Maiúsculas**:
   - O usuário poderá escolher se deseja ou não incluir letras maiúsculas na senha gerada.

4. **Opção para Incluir Números**:
   - O sistema permitirá que o usuário escolha se a senha incluirá números (0-9).

5. **Opção para Incluir Caracteres Especiais (Símbolos)**:
   - O usuário poderá decidir se deseja incluir caracteres especiais (como @, #, $, etc.) na senha.

6. **Limitação do Comprimento da Senha**:
   - O comprimento máximo da senha será limitado a 15 caracteres para garantir senhas práticas e seguras.

7. **Interface Simples via Linha de Comando**:
   - O script será operado via linha de comando, com prompts para o usuário configurar a senha conforme suas preferências.

## Cronograma de Desenvolvimento

O cronograma de desenvolvimento do projeto foi planejado em etapas claras, com prazos definidos para garantir que as funcionalidades sejam entregues de forma incremental e bem testada.

| Etapa                             | Descrição                                                                 | Prazo       |
|-----------------------------------|---------------------------------------------------------------------------|-------------|
| **1. Definição do Escopo e Planejamento** | Definir as funcionalidades principais do gerador de senhas.             | 1 dia       |
| **2. Implementação da Geração de Senha** | Desenvolver a função principal de geração de senhas aleatórias.           | 2 dias      |
| **3. Implementação de Opções de Configuração** | Implementar a configuração de letras maiúsculas, números e símbolos.      | 2 dias      |
| **4. Limitação de Comprimento da Senha** | Implementar a validação para limitar o comprimento máximo da senha.       | 1 dia       |
| **5. Testes e Depuração**         | Realizar testes para garantir que todas as opções e funcionalidades estão funcionando corretamente. | 2 dias      |
| **6. Documentação e Finalização** | Escrever a documentação no `README.md` e finalizar a implementação.     | 1 dia       |

**Total Estimado**: 9 dias

## Como Usar

1. Faça o download do script `geradsenhas.py`.
2. Execute o script no seu ambiente Python.

### Execução:
    
```bash
python geradsenhas.py

MIT License

Copyright (c) 2024 [Seu Nome ou Nome da Empresa]

Permissão é concedida, gratuitamente, a qualquer pessoa que obtenha uma cópia deste software e arquivos de documentação associados (o "Software"), para lidar no Software sem restrição, incluindo sem limitação os direitos de usar, copiar, modificar, mesclar, publicar, distribuir, sublicenciar e/ou vender cópias do Software, e para permitir que as pessoas a quem o Software é fornecido o façam, desde que a seguinte condição seja atendida:

A nota de copyright acima e esta permissão devem ser incluídas em todas as cópias ou partes substanciais do Software.

O Software é fornecido "como está", sem garantia de qualquer tipo, expressa ou implícita, incluindo, mas não se limitando a, garantias de comercialização, adequação a um propósito específico e não violação. Em nenhum caso os autores ou detentores dos direitos autorais serão responsáveis por qualquer reclamação, dano ou outra responsabilidade, seja em uma ação de contrato, ato ilícito ou outro, decorrente de, fora de ou em conexão com o Software ou o uso ou outros negócios no Software.


- Cawan Eduardo de Oliveira.
