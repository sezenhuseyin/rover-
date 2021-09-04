# rover-
Terminale Sırasıyla yazılması gerekenler

roscore

rosrun ilk_paket encoder_pub_node.py     //rastgele kodları dağıtan yer

rosrun ilk_paket subs_16.py              //16lık kodları alıp kontrol eden yer. Eğer başında a ve sonunda b harfleri varsa doğru kod kabul edip subs_16_executer a 
publishliyor

rosrun ilk_paket subs_24.py		          //24lük kodları alıp kontrol eden yer. Eğer başında a ve sonunda b harfleri varsa doğru kod kabul edip subs_24_executer a publishliyor

rosrun ilk_paket subs_16_executer.py	  //16lık kodları işleyip gerçek sayılara çeviriyor ve position/drive topici üzerinden publishliyor

rosrun ilk_paket subs_24_executer.py	  //24lük kodları işleyip gerçek sayılara çeviriyor ve position/robotic_arm topici üzerinden publishliyor

rosrun ilk_paket deneme_d.py            //açılmasına gerek yok. doğru publishlenmiş mi diye kontrol ettiğim yer

rosrun ilk_paket deneme_r.py            //açılmasına gerek yok. doğru publishlenmiş mi diye kontrol ettiğim yer
