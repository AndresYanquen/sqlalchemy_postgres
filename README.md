############################
QUERIES TO INSERT TEST DATA


-- Insert sample users
INSERT INTO users (username, email, full_name)
VALUES
    ('john_doe', 'john@example.com', 'John Doe'),
    ('jane_smith', 'jane@example.com', 'Jane Smith'),
    ('mike_jones', 'mike@example.com', 'Mike Jones'),
    ('sarah_adams', 'sarah@example.com', 'Sarah Adams');

-- Insert sample services
INSERT INTO services (service_name, description, price)
VALUES
    ('Haircut', 'Standard haircut service', 25),
    ('Massage', 'Relaxing full-body massage', 50),
    ('Manicure', 'Nail care and styling', 15),
    ('Facial', 'Skin rejuvenation treatment', 30);

-- Insert sample appointments
INSERT INTO appointments (user_id, service_id, scheduled_datetime)
VALUES
    (1, 1, NOW()),
    (1, 2, NOW() + INTERVAL '2 hours'),
    (2, 3, NOW() + INTERVAL '1 day'),
    (3, 1, NOW() + INTERVAL '3 days'),
    (3, 2, NOW() + INTERVAL '4 days'),
    (4, 4, NOW() + INTERVAL '5 days'),
    (2, 1, NOW() + INTERVAL '1 week'),
    (1, 3, NOW() + INTERVAL '10 days'),
    (4, 2, NOW() + INTERVAL '12 days'),
    (3, 4, NOW() + INTERVAL '2 weeks');