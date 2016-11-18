#OVERALL DESIGNSPECS  AND DESIGN NOTES


DOMAIN MODEL:

var Classroom = new mongoose.Schema({name: 'string', students: 'array', class_id: 'integer'})

var Student = new mongoose.Schema(
            {student_id: 'integer',
            name: 'string',
            class_id : 'integer',
            played_games: 'array'}
            )

var Game = new mongoose.Schema(
            {game_name : 'string',
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

####################################################

ASSOCIATED METHODS

Classroom.methods.addStudentstoArray = function addStudentstoArray () {
    # find students by class_id
        # if Classroom.id == Student.class_id
        #Classroom["students"] << Student
}

Game.methods.gamePlayed = function gamePlayed(){
    # once a student plays a game their data is saved in the DB
    # if game.student_id == student_id
        #Student["gamesplayed"] << Game
}
