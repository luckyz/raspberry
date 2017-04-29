# Customized aliases
alias pydir="cd ~/src/"
alias run="sudo python manage.py runserver 0.0.0.0:8000"
newpy(){
	cp "~/src/template/base.py" "$1.py"
}
