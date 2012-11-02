scriptexe = open("ALLExecute.sh", "w")

for subject in ['Arabi','Toma']:
    for query in ['Cocc','Hed','Indica','Lind','Lob','Nil','Pubes','Purp','Quamo']:
        if query!=subject:
            scriptname = query + '_to_' + subject + '.sh'
            
            shellscript = open(scriptname, "w")
            
            shellscript.write('#PBS -l walltime=20:00:00\n#PBS -l nodes=4:ppn=1\n#PBS -N Cenh3\n#PBS -j oe\n#PBS -S /bin/bash\n#PBS -m ae\ndate\ntrap "cd $PBS_O_WORKDIR;mkdir $PBS_JOBID;cp -R $TMPDIR/* $PBS_JOBID" TERM\n\n')
            shellscript.write('cd $HOME\n\n')
            
            shellscript.write('cp ./dbn/' + query + '.fasta $TMPDIR\n')
            shellscript.write('cp ./dbn/' + subject + '.fasta.nhr $TMPDIR\n')
            shellscript.write('cp ./dbn/' + subject + '.fasta.nin $TMPDIR\n')
            shellscript.write('cp ./dbn/' + subject + '.fasta.nsq $TMPDIR\n\n')
            
            shellscript.write('cd $TMPDIR\n\n')
            shellscript.write('/usr/local/biosoftw/blast-2.2.17/bin/blastall -a 4 -p blastn -i ' + query + '.fasta -d ' + subject + '.fasta -e .000001 -m 8 -o ' + query + '_to_' + subject + '.csv\n\n')
            shellscript.write('cp ' + query + '_to_' + subject + '.csv $HOME/ortho/rbh\n')
            shellscript.close()

            scriptexe.write('qsub ' + query + '_to_' + subject + '.sh\n')


for subject in ['Cocc','Hed','Indica','Lind','Lob','Nil','Pubes','Purp','Quamo']:
    for query in ['Arabi','Toma']:
        if query!=subject:
            scriptname = query + '_to_' + subject + '.sh'
            
            shellscript = open(scriptname, "w")
            
            shellscript.write('#PBS -l walltime=20:00:00\n#PBS -l nodes=4:ppn=1\n#PBS -N Cenh3\n#PBS -j oe\n#PBS -S /bin/bash\n#PBS -m ae\ndate\ntrap "cd $PBS_O_WORKDIR;mkdir $PBS_JOBID;cp -R $TMPDIR/* $PBS_JOBID" TERM\n\n')
            shellscript.write('cd $HOME\n\n')
            
            shellscript.write('cp ./dbn/' + query + '.fasta $TMPDIR\n')
            shellscript.write('cp ./dbn/' + subject + '.fasta.nhr $TMPDIR\n')
            shellscript.write('cp ./dbn/' + subject + '.fasta.nin $TMPDIR\n')
            shellscript.write('cp ./dbn/' + subject + '.fasta.nsq $TMPDIR\n\n')
            
            shellscript.write('cd $TMPDIR\n\n')
            shellscript.write('/usr/local/biosoftw/blast-2.2.17/bin/blastall -a 4 -p blastn -i ' + query + '.fasta -d ' + subject + '.fasta -e .000001 -m 8 -o ' + query + '_to_' + subject + '.csv\n\n')
            shellscript.write('cp ' + query + '_to_' + subject + '.csv $HOME/ortho/rbh\n')
            shellscript.close()

            scriptexe.write('qsub ' + query + '_to_' + subject + '.sh\n')

scriptexe.close()
