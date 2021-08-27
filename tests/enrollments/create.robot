***Settings***
Documentation       Gestão de Matriculla

Resource            ${EXECDIR}/resources/base.robot

Suite Setup         Start Admin Session
Test Teardown       Take Screenshot

***Test Cases***
Verificado data inicial e data final

    ${fixture}      Get JSON    enroll-dates.json

    ${aluno}        Set Variable    ${fixture['students']}
    ${plano}        Set Variable    ${fixture['plans']}

    Insert Student      ${aluno}
    Insert Plan         ${plano} 

    Go To Enrolls
    Go To Form Enrolls
    Select Student           ${aluno['name']}
    Select Plan              ${plano['title']}
    Start Date Should Today
    End Date Should Be       ${fixture['days']}

Matricula aluno em um plano
    ${fixture}      Get JSON    enroll-create.json

    ${aluno}        Set Variable    ${fixture['students']}
    ${plano_semestral}        Set Variable    ${fixture['plans']}

    Insert Student      ${aluno}
    Insert Plan         ${plano_semestral} 

    Go To Enrolls
    Go To Form Enrolls
    Select Student           ${aluno['name']}
    Select Plan              ${plano_semestral['title']}
    Submit Enrolls Form
    Toaster Text Should Be   Matrícula cadastrada com sucesso

    [Teardown]          Thinking And Take Screenshot  5

    