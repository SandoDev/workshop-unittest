# Workshop Uninttest

1. Introducción a la librería
 * Que testear

2. Creación del test por componente consultando directamente el servicio. `conf_test` file
3. Configuración en vscode

    ```
    Run and show in terminal
        ▶ pytest app --cov=app/
    Run and show in xml
        ▶ pytest app -rA --junit-xml=report_test/report-unit-test.xml
    Run with coverage and report html
        ▶ pytest app --cov=app --cov-report=html
        ▶ pytest app --cov=app --cov-report=xml
    ```

4. Creación del test por componente con mocks del servicio
5. Creacións reusables y modularizables mediante pluguins
