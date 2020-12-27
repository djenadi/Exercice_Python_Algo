

class BoardHelper(object):
    """
        Class Helper to resolve biggest square filling problem
    """
    def __init__(self, _file: str):
        """
            Take a filename containing a Tray and build it's matrix

            Args:
                _file: the file name to be readen
        """
        self.board = self.build_matrix_from_file(_file)

    def build_matrix_from_file(self, _file: str) -> list:
        """
            Build the board matrix for the given file name,
            this is done by validating the map config (validate_map_config),
            and parsing the file content (parse_content_to_matrix)

            Args:
                _file: the file name to be readen

        """
        try:
            _file = open(_file)
        except Exception as err:
            print(f"{err}")
            raise Exception('map error')

        try:
            board, all_lines, self.is_valid_map = [], _file.readlines(), False

            if all_lines:
                map_config = list(all_lines[0])

                # if there is content, we get map configuration
                self.rows_count, self.empty_char = ''.join(
                    map_config[:-4]), map_config[-4]
                self.obstacl_char, self.fill_char = map_config[-3], map_config[-2]
                self.is_valid_map = self.validate_map_config()

                # if valid map, we construct the matrix
                if self.is_valid_map:
                    board = self.parse_content_to_matrix(all_lines)

                return board

            return []

        except Exception as err:
            print(f"{err}")
            _file.close()
            return []

    def fill_biggest_square(self) -> str:
        """
            Make the new board containing the biggest square filled,

            Returns:
            The new filled board as string
        """
        if self.is_valid_map:
            star_index_i, start_index_j, len_ = self.get_biggest_square()
            filled_board = ""

            if len_:
                # replace square area by fill char
                for i in range(star_index_i, star_index_i + len_):
                    for j in range(start_index_j, start_index_j + len_):
                        self.board[i][j] = self.fill_char

            # Convert the matrix to string
            for i in range(0, self.rows_count):
                filled_board += f"{''.join(self.board[i])}\n"

            return filled_board
        else:
            raise Exception('map error')

    def get_biggest_square(self) -> tuple:
        """
            Search the biggest possible square of empty char in the board

            Returns:
                A tuple (start_index_i, start_index_j, len)
                    start_index_i, start_index_j represent
                    the coordinate of the biggest matrix.
                    len represent the size of the square
        """

        if self.board:
            rows_length, max_len = self.rows_count, 0
            cols_length = len(self.board[0]) if self.board else 0

            mat_sizes = [[0 for i in range(0, cols_length + 1)]
                         for i in range(0, rows_length + 1)]

            for i in range(1, rows_length + 1):
                for j in range(1, cols_length + 1):
                    if (self.board[i - 1][j - 1] == self.empty_char):
                        mat_sizes[i][j] = min(mat_sizes[i][j - 1],
                                              mat_sizes[i - 1][j],
                                              mat_sizes[i - 1][j - 1]) + 1

                        max_len = max(max_len, mat_sizes[i][j])

            for i in range(1, rows_length + 1):
                for j in range(1, cols_length + 1):
                    if mat_sizes[i][j] == max_len:
                        return i - 1 - (max_len - 1), j - 1 - \
                            (max_len - 1), max_len

        return 0, 0, 0

    def validate_map_config(self) -> bool:
        """
            Validate map configuration by checking the first char is an integer
            and each symbol is unique

            Returns:
                True if the map config is valid else False
        """
        try:
            self.rows_count = int(self.rows_count)
            map_allowed_symbol = [
                self.fill_char,
                self.empty_char,
                self.obstacl_char]

            # Check that there is at least one line
            if self.rows_count == 0:
                return False

            # Check unique symbole
            for char in map_allowed_symbol:
                if map_allowed_symbol.count(char) > 1:
                    return False

            return True
        except Exception as err:
            print(f"Map config validation err {err}")
            return False

    def parse_content_to_matrix(self, all_lines: list) -> list:
        """
            Construct the board matrix by parsing the readen file
            and validate each line, if one line is not valid when constructing,
            then the map is invalidated

            Args:
                all_lines: This is the first param.
            Returns:
                board: The constructed board matrix
        """

        board = []
        row_size = len(all_lines[1]) - 1
        try:

            for i in range(1, self.rows_count + 1):
                line = list(all_lines[i].replace("\n", ""))
                # Check that the line is well formatted
                if line.count(self.empty_char) + \
                        line.count(self.obstacl_char) != row_size:
                    self.is_valid_map = False
                    print('error : incorrect line format')
                    return board
                board.append(line)

        except Exception as err:
            print(f"{err}")
            self.is_valid_map = False

        return board
