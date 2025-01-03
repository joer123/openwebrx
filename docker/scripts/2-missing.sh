curl -s https://luarvique.github.io/ppa/openwebrx-plus.gpg | gpg --dearmor -o /etc/apt/trusted.gpg.d/openwebrx-plus.gpg
tee /etc/apt/sources.list.d/openwebrx-plus.list <<<"deb [signed-by=/etc/apt/trusted.gpg.d/openwebrx-plus.gpg] https://luarvique.github.io/ppa/debian ./"

curl -s https://repo.openwebrx.de/debian/key.gpg.txt | gpg --yes --dearmor -o /usr/share/keyrings/openwebrx.gpg
tee /etc/apt/sources.list.d/openwebrx.list <<<"deb [signed-by=/usr/share/keyrings/openwebrx.gpg] https://repo.openwebrx.de/debian/ bullseye main"

apt update
apt install -y libcsdr-dev csdr-cwskimmer
