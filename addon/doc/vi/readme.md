# Đồng hồ và Lịch cho NVDA

* Tác giả: Hrvoje Katić, Abdel và các cộng tác viên NVDA
* Tương thích với NVDA 2019.3 trở lên

Tiện ích này bổ sung các chức năng đồng hồ, hẹn giờ báo thức và lịch nâng cao cho NVDA.

Bạn có thể cấu hình NVDA để thông báo giờ và ngày theo các định dạng khác với định dạng mặc định của Windows. Ngoài ra, bạn có thể biết ngày hiện tại, số tuần trong năm cũng như số ngày còn lại trước khi kết thúc năm hiện tại, đồng thời cũng có thể thiết lập việc thông báo giờ tự động theo khoảng thời gian xác định. Tiện ích cũng tích hợp chức năng đồng hồ bấm giờ và hẹn giờ báo thức, cho phép bạn đo thời gian thực hiện các tác vụ như sao chép tệp, cài đặt chương trình hoặc nấu ăn.

Lưu ý:

* Nếu bạn cài đặt tiện ích dưới dạng bản cập nhật, trong quá trình cài đặt, trình hướng dẫn sẽ phát hiện xem cấu hình cũ có tương thích với cấu hình mới hay không và sẽ đề nghị sửa trước khi cài đặt. Sau đó, bạn chỉ cần nhấn nút "OK" để xác nhận.
* Trên Windows 10 trở lên, bạn có thể sử dụng ứng dụng Đồng hồ để quản lý đồng hồ bấm giờ và các bộ hẹn giờ.

## Các lệnh chính

* NVDA+F12: thông báo giờ hiện tại
* Nhấn nhanh NVDA+F12 hai lần: thông báo ngày hiện tại
* Nhấn nhanh NVDA+F12 ba lần: thông báo ngày hiện tại, số tuần, năm hiện tại và số ngày còn lại trước khi kết thúc năm
* NVDA+Shift+F12: vào lớp lệnh đồng hồ

## Các lệnh chưa được gán

Các lệnh sau chưa được gán cử chỉ theo mặc định. Nếu muốn gán, hãy sử dụng hộp thoại Cử chỉ nhập để thêm các lệnh tùy chỉnh. Để thực hiện, mở menu NVDA, chọn Tùy chọn, rồi Cử chỉ nhập. Mở rộng danh mục Đồng hồ, tìm một trong các lệnh chưa được gán dưới đây, chọn "Thêm", rồi nhập cử chỉ bạn muốn sử dụng.

* Thông báo thời gian đã trôi qua và thời gian còn lại trước báo thức tiếp theo. Nhấn nhanh cử chỉ này hai lần sẽ hủy báo thức tiếp theo.
* Dừng âm thanh báo thức đang phát.
* Hiển thị hộp thoại lập lịch báo thức.
* Hiển thị các lệnh của lớp lệnh (các phím cần nhấn sau NVDA+Shift+F12).

## Các lệnh theo lớp

Để sử dụng các lệnh theo lớp, nhấn NVDA+Shift+F12 rồi nhấn một trong các phím sau:

* S: khởi động, đặt lại hoặc dừng đồng hồ bấm giờ
* R: đặt lại đồng hồ bấm giờ về 0 mà không khởi động lại
* A: thông báo thời gian đã trôi qua và thời gian còn lại trước báo thức tiếp theo
* T: mở hộp thoại lập lịch báo thức.
* C: hủy báo thức tiếp theo
* Phím cách: đọc trạng thái hiện tại của đồng hồ bấm giờ hoặc bộ đếm ngược
* P: nếu âm thanh báo thức kéo dài quá lâu, cho phép dừng báo thức
* H: liệt kê tất cả các lệnh theo lớp (Trợ giúp)

## Cấu hình và sử dụng

Để cấu hình chức năng đồng hồ, mở menu NVDA, chọn Tùy chọn, rồi Cài đặt, sau đó cấu hình các tùy chọn sau trong danh mục Đồng hồ:

* Định dạng hiển thị giờ và ngày: sử dụng các hộp kết hợp này để cấu hình cách NVDA thông báo giờ và ngày khi bạn nhấn NVDA+F12 một lần hoặc nhấn nhanh hai lần tương ứng.
* Khoảng thời gian: chọn khoảng thời gian thông báo giờ từ hộp kết hợp này (tắt, mỗi 10 phút, 15 phút, 30 phút hoặc mỗi giờ).
* Thông báo giờ (được bật nếu khoảng thời gian không tắt): chọn giữa giọng nói và âm thanh, chỉ âm thanh hoặc chỉ giọng nói.
* Âm thanh điểm chuông đồng hồ (được bật nếu khoảng thời gian không tắt): chọn âm thanh điểm chuông mặc định cho các phút trung gian và đầu mỗi giờ.
* Tách riêng âm báo đầu giờ và các phút trung gian (được bật nếu khoảng thời gian không tắt, mặc định bị tắt): đánh dấu hộp kiểm này để tùy chỉnh riêng âm báo cho các phút trung gian và âm báo đầu giờ.
  * Âm thanh điểm chuông cho các phút trung gian (được bật nếu chọn "Tách riêng âm báo đầu giờ và các phút trung gian"): chọn âm thanh điểm chuông dành riêng cho các phút trung gian.
* Giờ yên tĩnh (được bật nếu khoảng thời gian không tắt): chọn hộp kiểm này để cấu hình khoảng thời gian yên tĩnh, trong đó việc thông báo giờ tự động sẽ không diễn ra.
* Định dạng thời gian của giờ yên tĩnh (được bật nếu giờ yên tĩnh được bật): chọn cách hiển thị các tùy chọn giờ yên tĩnh (định dạng 12 giờ hoặc 24 giờ).
* Thời gian bắt đầu và kết thúc giờ yên tĩnh: chọn khoảng giờ và phút cho giờ yên tĩnh từ các hộp kết hợp giờ và phút.

Để lập lịch báo thức, mở menu NVDA, chọn Công cụ, rồi chọn Lập lịch báo thức. Hộp thoại bao gồm các thành phần sau:

* Thời lượng báo thức theo: chọn thời lượng báo thức/hẹn giờ theo giờ, phút hoặc giây.
* Thời lượng: nhập thời lượng báo thức theo đơn vị đã chọn ở trên.
* Âm thanh báo thức: chọn âm thanh sẽ được phát khi báo thức kích hoạt.
* Các nút Dừng và Tạm dừng: dừng hoặc tạm dừng âm thanh báo thức kéo dài.

Nhấn OK, một thông báo sẽ cho bạn biết thời lượng báo thức hiện đang được chọn.
