#################
# GROUP MEMBERS #
#################
#
#
#
##################
declare -a calledInts
declare -a marked
marked[0]='00'
index=0
printCard (){
    printf "L \t I \t N \t U \t X"
    for i in {1..5}
do
printf "\n"
j=0
    for y in {1..${#x[$i]}} #print each elements
    do
        printf "$(echo ${x[i]}| cut -d' ' -f 1) \t $(echo ${x[i]}| cut -d' ' -f 2) \t $(echo ${x[i]}| cut -d' ' -f 3) \t $(echo ${x[i]}| cut -d' ' -f 4) \t $(echo ${x[i]}| cut -d' ' -f 5) \n"
        #echo "${x[i]}"
        ((j++))
    done
done
}
mainLoop (){
    setM="00"
    while [ 1 -eq 1 ]
    do
        #clear
        printf "Enter any key to get a call or q to quit: "
        read choice
        winningCondition
        winningFlag=$?
        if [ $choice = 'q' ]
        then
            break
        fi
        if [ $winningFlag = '1' ]
        then
            echo "WINNER"
            break
        fi
        clear
        guess=$RANDOM
        calledInts[$index]=$(( guess %= 75 ))
        #print called numbers
        j=0
        printf "CALL LIST: "
        for i in "${calledInts[@]}"
        do
            if [ $i -gt 0 ] && [ $i -lt 16 ]
            then
                printf "L${calledInts[$j]} "
            fi
            if [ "$i" -gt "15" ] && [ "$i" -lt "31" ]
            then
                printf "I${calledInts[$j]} "
            fi
            if [ "$i" -gt "30" ] && [ "$i" -lt "46" ]
            then
                printf "N${calledInts[$j]} "
            fi
            if [ "$i" -gt "45" ] && [ "$i" -lt "61" ]
            then
                printf "U${calledInts[$j]} "
            fi
            if [ "$i" -gt "60" ] && [ "$i" -lt "76" ]
            then
                printf "X${calledInts[$j]} "
            fi
            ((j++))            
        done
        printf "\n"
        #Check for matching numbers
        for i in {1..5}
        do
            x=${x[i]}
            if [ ${#guess} == 1 ]
            then
                guess="0"$guess
            fi
            prefix=${x%%$guess*}
            position=${#prefix}
            m=${x:0:(($position+2))}
            n=${x:(($position+2)):${#x}}

            if [ $position -lt ${#x} ]
            then
                x=${x:0:(($position+2))}"m"" "${x:(($position+2)):${#x}}
            fi
            x[$i]=$x
        done
        #set m to 00
        if [ $setM = "00" ]
        then
            x=${x[3]}
            rule0="00"
            prefix=${x%%$rule0*}
            position=${#prefix}
            m=${x:0:(($position+2))}
            n=${x:(($position+2)):${#x}}
            x[3]=${x:0:(($position+2))}"m"" "${x:(($position+2)):${#x}}
            setM="01"
        fi
        printCard
        ((index++))
    done
}
winningCondition (){
    #loop through each column and through each row
    #each row is holding x constant
    local win=0
    for i in {1..5}
    do
        #select one value in the row to be equated to
        temp1=$(echo ${x[i]}| cut -d' ' -f 1)
        temp2=$(echo ${x[i]}| cut -d' ' -f 2)
        temp3=$(echo ${x[i]}| cut -d' ' -f 3)
        temp4=$(echo ${x[i]}| cut -d' ' -f 4)
        temp5=$(echo ${x[i]}| cut -d' ' -f 5)        
        if [ ${#temp1} -gt 2 ] && [ ${#temp2} -gt 2 ] && [ ${#temp3} -gt 2 ] && [ ${#temp4} -gt 2 ] && [ ${#temp5} -gt 2 ]
        then
            local win=1
        fi
    done
    #each column is 
    for i in {1..5}
    do
        #select one value in the column to be equated to
        local temp1=$(echo ${x[$i]}| cut -d' ' -f 1)
        local temp2=$(echo ${x[$i]}| cut -d' ' -f 2)
        local temp3=$(echo ${x[$i]}| cut -d' ' -f 3)
        local temp4=$(echo ${x[$i]}| cut -d' ' -f 4)
        local temp5=$(echo ${x[$i]}| cut -d' ' -f 5)
        if [ ${#temp1} -gt 2 ] && [ ${#temp2} -gt 2 ] && [ ${#temp3} -gt 2 ] && [ ${#temp4} -gt 2 ] && [ ${#temp5} -gt 2 ]
        then
            local win=1
        fi
    done
    #the 4 corners
    choosenCorner=$(echo ${x[5]}| cut -d' ' -f 5)
    if [ $(echo ${x[1]}| cut -d' ' -f 1) = $choosenCorner ] && [ $(echo ${x[1]}| cut -d' ' -f 5) = $choosenCorner ] && [ $(echo ${x[5]}| cut -d' ' -f 1) = $choosenCorner ]
    then
        local win=1
    fi
    #win=1
    return $win
}

if [ -r "$1" ] #Check if file exists
then
    fileLines () {
        cat $1 | wc -l
    }
    let nLines=$( fileLines $1 )+1
    seed=${x[0]}
    if [ $nLines -eq 6 ] #Check if the file has 6 lines
    then
        #populate array x with the rows/lines
        #declare -a x
        counter=0
        while read line
        do
            x[$counter]=$line
            #echo ${x[$counter]}
            ((counter++)); 
        done < <({ cat $1; echo; })
        #echo ${x[0]}
        if [[ "${x[0]}" =~ ^[0-9]+$ ]] # Check if seed line is correct i.e. contains non digit characters
        then
            #echo "Seed all good"
            #check if all variables are perfect
            #create flag if 1 continue if 0 stop
            for i in {1..5}
            do
                for y in ${x[$i]}
                do
                    #echo $y
                    if [ ${#y} -lt 2 ] || [ ${#y} -gt 2 ]
                    then
                        flag=0
                        #echo "Flag changed at: $y"
                        break
                    else
                        #echo "Flag REVERTED at: $y"
                        flag=1
                    fi
                done
                if [ $flag -eq 0 ]
                then
                    break
                fi
            done
            #echo "Value of flag $flag"
            if [ $flag -eq 1 ] #Main code
            then
                echo "Good input 0"
                mainLoop
                echo "exit 0."
            else
                echo "exit 4. \"card format error\""
            fi
        else
            echo "exit 3. \"seed line format error\""
        fi
    else
        echo "exit 2. \"input file must have 6 lines\""
    fi
else
    echo "exit 1. \"input file missing or unreadable\""
fi
