Theorem ch2:forall P Q:Prop,
  (P->Q)->(~Q->~P).
Proof.
intros.
unfold not in H0.
unfold not.
intros.
apply H0 in H.
apply H.
apply H1.
Qed.
