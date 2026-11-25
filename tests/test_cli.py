from main import main

def test_cli_success():
    # Запускаем main с аргументами и проверяем код возврата (0 = успех)
    exit_code = main(["--kind", "sine", "--n", "5", "--window", "2"])
    assert exit_code == 0

def test_cli_error_invalid_n():
    # n=-1 должно вернуть код ошибки 1
    exit_code = main(["--kind", "sine", "--n", "-1"])
    assert exit_code == 1