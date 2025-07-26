import project


def test_check_for_win():

    board = {
        1: "X", 2: "X", 3: "X",
        4: "", 5: "", 6: "",
        7: "", 8: "", 9: ""
    }
    assert project.Check_For_Win("X", board) == True
    print("test_check_for_win passed.")

def test_check_for_draw():

    board = {
        1: "X", 2: "O", 3: "X",
        4: "X", 5: "O", 6: "O",
        7: "O", 8: "X", 9: "X"
    }
    assert project.Check_For_Draw(board) == True
    print("test_check_for_draw passed.")

def test_insert(monkeypatch):

    board = {i: "" for i in range(1, 10)}
    board[1] == "X"

    inputs = iter(["1", "2"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    project.insert("0", 1, board)

    assert board[2] == "0"
    print("test_insert passed.")


if __name__ == "__main__":
    test_check_for_win()
    test_check_for_draw()
    test_insert
