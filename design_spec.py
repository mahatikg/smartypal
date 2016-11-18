#OVERALL DESIGNSPECS  AND DESIGN NOTES


DOMAIN MODEL:

var Classroom = new mongoose.Schema({name: 'string', students: 'array'})

var Student = new mongoose.Schema(
            {student_id: 'integer',
            name: 'string',
            class_id : 'integer',
            played_games: 'array'}
            )

var Game = new mongoose.Schema(
            {game_name : 'string',
            students : [ array of students ]
            time : 'integer', # potentially >> {total: 45, time_taken: 32}
            problems_total : 'integer',
            problems_finished : 'integer',
            problems_correct : 'integer',
            problems_incorrect : 'array'

            # also possible for greater data extraction:
                            {incorrect:  3,
                            details : [
                             {
                                'question_num': 1,
                                'core_concept': 'addition'
                                'secondary_concept' : 'factorization'
                             },
                             {another question doc that details the data of the particular question student got wrong}

                             ]}
        'percentage' : '70%' })

###########################################################


TENTATIVE DOCUMENTS AND COLLECTIONS:

#API/vi/sendmetrics
data = { class_data:{
        'name' : 'Ms. Abbey 3rd Grade',
        'students' : [ {}, {},{} ]
} }

Associated Methods:

Classroom.methods.addStudentstoArray = function addStudentstoArray () {
  return add Student documents with correct_ids into to the students array
}

Game.methods.didStudentplay = function didStudentplay (){
    return push into array the student document of the student who played the game
}
