INSERT INTO App_Usuario (password, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, rut, telefono, modification_date) VALUES
('1234', 'false', 'cliente 1', 'A', 'A', 'a@mail.com', 'false', 'true', CURRENT_TIMESTAMP, '11111111-1', '+56 9 11111111', CURRENT_TIMESTAMP),
('1234', 'false', 'cliente 2', 'B', 'B', 'b@mail.com', 'false', 'true', CURRENT_TIMESTAMP, '22222222-2', '+56 9 22222222', CURRENT_TIMESTAMP),
('1234', 'false', 'cliente 3', 'C', 'C', 'c@mail.com', 'false', 'true', CURRENT_TIMESTAMP, '33333333-3', '+56 9 33333333', CURRENT_TIMESTAMP),
('1234', 'false', 'repartidor 1', 'D', 'D', 'd@mail.com', 'false', 'true', CURRENT_TIMESTAMP, '44444444-4', '+56 9 44444444', CURRENT_TIMESTAMP);

INSERT INTO App_Cliente (usuario_id) VALUES
('11111111-1'),
('22222222-2'),
('33333333-3');

INSERT INTO App_Repartidor (usuario_id) VALUES
('44444444-4');

INSERT INTO App_Warehouse (location_lon, location_lat) VALUES
(-73.0398162, -36.8267985),
(-73.0477251, -36.8284895);

INSERT INTO App_Truck (capacity_x, capacity_y, capacity_z, warehouse_id) VALUES
(1, 1, 1, 1),
(1, 1, 1, 1),
(1, 1, 1, 2);

INSERT INTO App_DeliveryOrder (destination_lon, destination_lat, dim_x, dim_y, dim_z, weight, registration_date, client_id, warehouse_id) VALUES
(-73.0479204472459, -36.82315836901451, 1, 1, 1, 1, CURRENT_TIMESTAMP, 3, 1),
(-73.0419427136815, -36.82221818010478, 1, 1, 1, 1, CURRENT_TIMESTAMP, 3, 1),
(-73.0620552425805, -36.82201695816364, 1, 1, 1, 1, CURRENT_TIMESTAMP, 3, 1),
(-73.1042940323166, -36.84138561881967, 1, 1, 1, 1, CURRENT_TIMESTAMP, 3, 2),
(-73.0587175028952, -36.83379092608528, 1, 1, 1, 1, CURRENT_TIMESTAMP, 1, 1),
(-73.0557893516289, -36.84075446927645, 1, 1, 1, 1, CURRENT_TIMESTAMP, 1, 2),
(-73.1046796925466, -36.83958985489116, 1, 1, 1, 1, CURRENT_TIMESTAMP, 2, 1),
(-73.1166176296651, -36.83319210321522, 1, 1, 1, 1, CURRENT_TIMESTAMP, 2, 2),
(-73.1174590701668, -36.83319210321522, 1, 1, 1, 1, CURRENT_TIMESTAMP, 2, 2),
(-73.1174590701668, -36.84051580093253, 1, 1, 1, 1, CURRENT_TIMESTAMP, 1, 1),
(-73.0535047463489, -36.82198925939674, 1, 1, 1, 1, CURRENT_TIMESTAMP, 3, 2),
(-73.0578264668393, -36.84084003585665, 1, 1, 1, 1, CURRENT_TIMESTAMP, 2, 2);