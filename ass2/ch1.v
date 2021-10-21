Theorem ch1:forall P Q R:Prop,
  (P/\Q->R)<->(P->Q->R).
Proof.
intros.
split.
intros.
apply H.
split.
apply H0.
apply H1.
intros.
apply H.
apply H0.
inversion H0.
apply H2.
Qed.
