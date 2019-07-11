# Đồng hồ và lịch Add-on cho NVDA #

* Tác giả: Hrvoje Katić, Abdel và cộng tác viên NVDA;
* Tải về [phiên bản chính thức][1];
* Tải về [phiên bản thử nghiệm][2].


Addon này cung cấp tính năng nâng cao cho đồng hồ, báo giờ và lịch cho NVDA.

Thay vì luôn lấy thông tin ngày giờ từ Windows, bạn có thể tùy biến cách mà
NVDA đọc và hiển thị ngày giờ trong chữ nổi.

Thêm nữa, bạn có thể lấy thông tin về ngày hiện tại, số tuần, kể cả số ngày
còn lại trước khi kết thúc năm, và bạn cũng có thể đặt báo giờ tự động trong
khoảng thời gian nhất định.

Có cả đồng hồ bấm giờ và tính năng báo giờ được tích hợp trong addon để hẹn
giờ cho công việc của bạn, chẳng hạn như chép các tập tin, cài đặt chương
trình hay nấu ăn.

## Lưu ý:

Nếu bạn cài đặt add-on ở dạng cập nhật, trong khi thực hiện cài đặt, chương
trình sẽ kiểm tra việc cấu hình cũ có tương thích với phiên bản mới và chỉnh
sửa chúng trước khi cài đặt, rồi thì bạn chỉ việc bấm nút Đồng Ý để xác
nhận.

## Sử dụng

* Mở hộp thoại cấu hình cho addon này từ trình đơn công cụ của NVDA hoặc từ
  bản tùy chỉnh tùy theo phiên bản NVDA của bạn;

    * Trong hộp thoại cài đặt đồng hồ, hai hộp xổ đầu tiên cho phép bạn chọn
      kiểu hiển thị ngày giờ ưa thích của mình;
    * Hộp xổ tên "Khoảng thời gian" cho phép bạn đặt thời gian báo giờ tự
      động (mỗi 10 phút, mỗi 15 phút, mỗi 30 phút, mỗi giờ, hoặc là tắt);
    * Hộp xổ tên "Báo giờ" (chỉ hiển thị khi lựa chọn "tắt" không được chọn
      từ hộp xổ khoảng thời gian) cho phép bạn cấu hình việc tự báo giờ (nói
      và âm thanh, chỉ nói, hay chỉ âm thanh) khi tính năng tự báo giờ hoạt
      động;
    * Hộp xổ tên "Chuông đồng hồ" (chỉ hiển thị khi lựa chọn "tắt" không
      được chọn trong hộp xổ khoảng thời gian) cho phép bạn chọn giữa nhiều
      chuông đồng hồ sẽ được phát khi tính năng tự báo giờ hoạt động và
      thông báo bằng âm thanh;
    * Hộp kiểm tên "Giờ yên tĩnh" (chỉ hiển thị khi lựa chọn "tắt" không
      được chọn trong hộp xổ khoảng thời gian) cho phép bạn cấu hình khoảng
      thời gian mà tính năng tự báo giờ không nên hoạt động;
    * Hộp kiểm tên "Nhập định dạng 24 giờ" (chỉ hiển thị khi giờ yên tĩnh
      được bật) cho phép bạn cấu hình cách nhập thời gian cho giờ yên tĩnh
      theo kiểu 12 giờ (A.M. hoặc P.M.) hay định dạng 24 giờ - giờ Châu Âu;
    * Các ô nhập liệu cho thời gian bắt đầu và kết thúc (chỉ hiển thị khi
      giờ yên tĩnh được bật) cho phép bạn cấu hình khoảng thời gian của giờ
      yên tĩnh. Thời gian phải được nhập là HH:MM nếu đã chọn hộp kiểm "Nhập
      định dạng 24 giờ", nếu không. bạn phải dùng kiểu định dạng 12 giờ được
      mô tả bên dưới;
    * Khi hoàn tất, tab đến nút Đồng Ý và kích hoạt nó bằng Enter để lưu
      thiết lập;
    * Trong hộp thoại cài đặt báo hiệu, hộp xổ đầu tiên cho phép bạn chọn
      kiểu thời gian đếm ngược trước khi phát báo hiệu;
    * Ô nhập liệu cho phép bạn nhập thời gian chờ trước khi phát báo
      hiệu. Thời gian này phải được nhập là một hay nhiều số tự nhiên, không
      phải số thập phân;
    * Hộp xổ tên "Âm báo hiệu" cho phép bạn chọn giữa nhiều âm báo hiệu sẽ
      được phát khi đến giờ báo hiệu;
    * Nút tạm dừng cho phép bạn tạm dừng / tiếp tục báo hiệu dài;
    * Nút dừng cho phép bạn dừng báo hiệu dài;
    * Khi hoàn tất, tab đến nút Đồng Ý và kích hoạt nó bằng Enter. Một thông
      điệp sẽ hiển thị, nhắc bạn thời gian chờ trước khi báo hiệu;

* Bấm NVDA+F12 một lần để xem giờ hiện tại, hai lần để xem ngày hiện tại,
  hay ba lần để xem ngày hiện tại, số tuần, kể cả số ngày còn lại trước khi
  kết thúc năm hiện tại.

## Các phím lệnh

* NVDA+F12, xem giờ hiện tại;
* NVDA+F12 bấm nhanh hai lần, xem ngày hiện tại;
* NVDA+F12 bấm nhanh ba lần, thông báo ngày hiện tại, số tuần, năm hiện tại
  và số ngày còn lại trước khi kết thúc năm.
* Có một kịch bản cung cấp cho bạn thời gian đã qua và thời gian còn lại
  trước khi có báo hiệu tiếp theo;
* Không có thao tác cho kịch bản này. bạn phải tự gán lệnh trong hộp thoại
  "Quản lý các thao tác", trong phân loại Đồng hồ";
* Thực hiện thao tác này nhanh hai lần để hủy bỏ báo hiệu kế tiếp;
* Còn có một kịch bản khác để dừng âm thanh đang được phát. Thao tác này
  cũng không được quy định;
* Cũng có thể gọi các kịch bản đó bằng các lệnh layer được mô tả dưới đây.

## Các lệnh layer

Để dùng các lệnh layer, bấm NVDA+Shift+F12 rồi một trong các phím sau:

* S: Bắt đầu, đặt lại hay dừng đồng hồ bấm giờ;
* R: đặt lại đồng hồ báo giờ là 0 mà không khởi động lại nó;
* A: cung cấp thời gian đã qua và còn lại trước báo hiệu tiếp theo;
* C: hủy báo hiệu tiếp theo;
* Khoảng trắng: thông báo đồng hồ bấm giờ hay thời gian đếm ngược hiện tại;
* p: nếu báo hiệu quá dài thì cho phép dừng lại;
* H: liệt kê tất cả lệnh layer.

## Cú pháp dùng cho giờ yên tĩnh

* Để tránh gây ra lỗi, giờ yên tĩnh phải tuân theo các cú pháp chặt chẽ và
  chính xác;
* Nếu bạn chọn hộp kiểm "Nhập định dạng 24 giờ", định dạng sẽ phải là
  "HH:MM";
* Nếu bạn không chọn hộp kiểm "Nhập định dạng 24 giờ", định dạng sẽ phải là
  "HH:MM AM" hay "HH:MM PM", HH phải là kiểu định dạng 12 giờ, từ 0 đến 12
  và hậu tố "AM"|"PM" có thể là chữ hoa hoặc thường
* Nếu chọn vào hộp kiểm Giờ yên tĩnh" và để trống mục "Thời gian bắt đầu giờ
  yên tĩnh" hoặc "Thời gian kết thúc giờ yên tĩnh", hoặc nhập một giá trị
  sai, hộp kiểm "Giờ yên tĩnh" sẽ tự bị bỏ chọn để tránh xảy ra lỗi;
* Một thông điệp sẽ hiển thị để báo lỗi.

## Tính tương thích

* Add-on này tương thích với các phiên bản NVDA từ 2014.3 đến 2019.3.


[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cac

[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev

