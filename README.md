# Hướng dẫn sử dụng chương trình

## Để  thực hiện câu truy vấn, sửa các trường trong file utils/statement_compare.json:
- Trường "select" : Lựa chọn khái niệm/thuộc tính của khái niệm muốn truy vấn
- Trường "where"  : Điều kiện để  thực hiện truy vấn
    - Trường "compare" là một phép kiểm tra một biểu thức
        - "keyword" : Trường thông tin muốn kiếm tra
        - "comparator": Phép so sánh
        - "expression" : Biểu thức muốn kiểm tra
    - Trường "logic" là một phép giao/hợp các điều kiện
    - Trường "in-bracket" dùng để  xác định thứ tự thực hiện việc kiểm tra các điều kiện.

## Để  thực hiện một luật:
- Trường "if" là điều kiện cần kiểm tra để thực hiện luật
- Trường "then" gồm các hành động sẽ được thực hiện nếu điều kiện trong trường "if" là đúng
- Trường "else" gồm các hành động sẽ được thực hiện nếu điều kiện trong trường "if" là sai. Trường này có thể không có

## Chạy file language/run.py sử dụng python3