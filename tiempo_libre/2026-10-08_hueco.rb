# hueco.rb — la biblioteca de fechas de Ruby nombra la reforma por país.
# Uso: ruby hueco.rb
require 'date'
D = %w[domingo lunes martes miércoles jueves viernes sábado]
puts "Date::ITALY   = #{Date::ITALY}  (día juliano del corte por defecto) -> #{Date.jd(Date::ITALY, Date::ITALY)}"
puts "Date::ENGLAND = #{Date::ENGLAND} -> #{Date.jd(Date::ENGLAND, Date::ENGLAND)}"
puts "¿existe el 8/10/1582? por defecto (ITALY): #{Date.valid_date?(1582, 10, 8)} | con ENGLAND: #{Date.valid_date?(1582, 10, 8, Date::ENGLAND)}"
begin
  Date.new(1582, 10, 8)
rescue => e
  puts "Date.new(1582,10,8) -> #{e.class}: #{e.message}"
end
puts "4/10/1582 + 1 = #{Date.new(1582, 10, 4) + 1}"
d = Date.new(1584, 10, 8)
puts "8/10/1584 por defecto: #{D[d.wday]} (gregoriano)"
# un corte cordobés: todavía juliano el 1/1/1585, ya gregoriano el 9/6/1585.
# No se sabe el día; pongo el corte en cualquier punto de ese intervalo para mostrar que alcanza.
corte = Date.new(1585, 6, 1, Date::GREGORIAN).jd
c = Date.new(1584, 10, 8, corte)
puts "8/10/1584 con corte cordobés (JD #{corte}): #{D[c.wday]}  = #{c.new_start(Date::GREGORIAN)} en gregoriano"
puts "1/1/1585 con corte cordobés: #{D[Date.new(1585, 1, 1, corte).wday]} | 16/6/1585: #{D[Date.new(1585, 6, 16, corte).wday]}"
puts "11/6/1580 (antes de cualquier corte): #{D[Date.new(1580, 6, 11).wday]} = #{Date.new(1580, 6, 11).new_start(Date::GREGORIAN)} en gregoriano proléptico"
hoy = Date.new(2026, 10, 8)
puts "hoy, 8/10/2026, en juliano: #{hoy.new_start(Date::JULIAN)}"
